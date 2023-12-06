from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password ,check_password 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .models import CustomUser
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

# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def custom_user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Ensure both username and password are provided
    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve the user by username
    user = CustomUser.objects.filter(userName=username).first()

    if user and (password == user.password):
        # Password is correct
        # Serialize the user data
        serializer = CustomUserSerializer(user)
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        print(serializer.data,"gjhgkj",data)

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

    if serializer.is_valid():
        user = serializer.save()  # Save the user instance
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def taskUpdate(request):
        # user_id = request.user.id
        # task= CustomUser.objects.get(U_id=user_id)
        # serializer = CustomUserSerializer(instance=task, data=request.data)
        
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
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

	    # if serializer.is_valid():
		#     serializer.save()


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def task_update(request):
#     user_id = request.user.id

    # try:
    #     task = CustomUser.objects.get(U_id=user_id)
    # except CustomUser.DoesNotExist:
    #     return Response({"error": "Task not found for the current user"}, status=404)

    # serializer = CustomUserSerializer(instance=task, data=request.data)

    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     return Response(serializer.errors, status=400)
@api_view(['DELETE'])
def delete_all_custom_users(request):
    try:
        CustomUser.objects.all().delete()
        return Response({'message': 'All CustomUser rows deleted successfully'})
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=500)


