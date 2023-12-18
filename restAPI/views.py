from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password ,check_password 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .serializers import CustomUserSerializer ,QuestionSerializer , AnswersSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .models import CustomUser , Question , Answers
from django.contrib.auth import authenticate
import bcrypt
from .token_utils import get_user_id_from_token
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def getUsers(request):
	users = CustomUser.objects.all()
	serializer = CustomUserSerializer(users, many=True)
	return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
def custom_user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Ensure both username and password are provided
    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve the user by username
    user = CustomUser.objects.filter(userName__iexact=username).first()
    
    if user and (str(password) == str(user.password)):
        # Password is correct
        # Serialize the user data
        
        serializer = CustomUserSerializer(user)
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
      
        return Response({
            'Token':data,
            'user': serializer.data,
            'api_status':True
        })
    else:
        # Invalid username or password
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def user_create(request):
    serializer = CustomUserSerializer(data=request.data)
    utype = request.data.get('userType')
    print(utype)
    if serializer.is_valid():
        user = serializer.save()  # Save the user instance
        refresh = RefreshToken.for_user(user)
        data2= serializer.data
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user':data2
        }
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def taskUpdate(request):
        user_id = get_user_id_from_token(request)
        
        if user_id is not None:
                try:
                    task = CustomUser.objects.get(U_id=user_id)
                except CustomUser.DoesNotExist:
                      return Response({"error": "Task not found for the current user"}, status=404)
                serializer = CustomUserSerializer(instance=task, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=400)

        else:
            return  Response(status=401) 

	 

@api_view(['DELETE'])
def delete_all_custom_users(request):
    try:
        CustomUser.objects.all().delete()
        return Response({'message': 'All CustomUser rows deleted successfully'})
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=500)


# create question view 
@api_view(['POST'])
def create_question(request):
    # Get user ID from token
    user_id = get_user_id_from_token(request)

    if user_id is not None:
        # Retrieve user instance based on user ID
        try:
            user = CustomUser.objects.get(U_id=user_id)
            # print(user,"jdnsdnsdk")
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create a new question with user association
        request.data['user_id'] = user_id
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['user'] = user  # Associate the question with the user
            serializer.save(user_id=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Authentication token not valid"}, status=status.HTTP_401_UNAUTHORIZED)

# get all questions 
@api_view(['GET'])
def getQuestion(request):
	question = Question.objects.all()
	serializer = QuestionSerializer(question, many=True)
    
	return Response(serializer.data)

# ----------------------------Answer a question ---------------------------------------#
# create question view 
@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def answer_question(request):
    # Get user ID from token
    user_id = get_user_id_from_token(request)

    if user_id is not None:
        # Retrieve user instance based on user ID
        try:
            user = CustomUser.objects.get(U_id=user_id)
            # print(user,"jdnsdnsdk")
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create a new question with user association
        request.data['user_id'] = user_id
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['user'] = user  # Associate the question with the user
            serializer.save(user_id=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Authentication token not valid"}, status=status.HTTP_401_UNAUTHORIZED)

# --------------------------get answers for Question-----------------------------------#
@api_view(['POST'])
def getAnswersForQuestion(request):

    # Assuming Q_id is present in the request data
    q_id = request.data.get('Q_id')

    if q_id is not None:
        # Use filter to get answers for a specific question
        answers = Answers.objects.filter(Q_id=q_id)
        count_of_question = answers.count()
        serializer = AnswersSerializer(answers, many=True)
        data = {
            'count_of_anser' :  count_of_question,
            'data': serializer.data ,
            'message' : 'aswers for question',
            'api_status' : 200
        }
        return Response(data)
    else:
        return Response({"error": "Q_id is required in the request data"}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------delete question ----------------------------------------#
@api_view(['POST'])
def deteleQuestion(request):
    user_id = get_user_id_from_token(request)
    if user_id is not None:
        # Retrieve user instance based on user ID
        Q_id = request.data.get('Q_id')
        try:
            question = Question.objects.get(Q_id=Q_id)
            Serializer = QuestionSerializer(question, many=False)
            if str(user_id) != str(question.user_id):    # note  convert  <class 'restAPI.models.CustomUser'> = question.user_id  in to string 
                return Response({"error": "You do not have permission to delete this question.",
                "userids" :f"user->{type(user_id)} questio {type(question.user_id)}"
                }, status=status.HTTP_403_FORBIDDEN)

            # Delete the question
            question.delete()

            return Response({"message": f"Question with id {Q_id} deleted successfully"
            "userids"
            }, status=status.HTTP_204_NO_CONTENT)

        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({"error": "Authentication token not valid"}, status=status.HTTP_401_UNAUTHORIZED)


#--------------------------------delete answer -----------------------------------------------------#
@api_view(['POST'])
def deteleAnswer(request):
    user_id = get_user_id_from_token(request)
    if user_id is not None:
        # Retrieve user instance based on user ID
        A_id = request.data.get('A_id')
        try:
            answer = Answers.objects.get(A_id=A_id)
            # Serializer = QuestionSerializer(question, many=False)
            if str(user_id) != str(answer.user_id):    # note  convert  <class 'restAPI.models.CustomUser'> = question.user_id  in to string 
                return Response({"error": "You do not have permission to delete this question.",
                "userids" :f"user->{type(user_id)} questio {type(answer.user_id)}"
                }, status=status.HTTP_403_FORBIDDEN)

            # Delete the question
            answer.delete()

            return Response({"message": f"Answer with id {A_id} deleted successfully"
            "userids"
            }, status=status.HTTP_204_NO_CONTENT)

        except Answers.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({"error": "Authentication token not valid"}, status=status.HTTP_401_UNAUTHORIZED)

#-------------------------------- like  question -------------------------------------------#
