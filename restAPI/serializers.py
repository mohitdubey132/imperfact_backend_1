from rest_framework import serializers
from .models import CustomUser ,Question , Answers

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['U_id', 'userType','userName','fullName','age','gender','address','mobileNo', 'country']
        
#-----------------for use in other Serializer --------------------------------------------------# 
class CustomUtilsUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =[ 'userType','userName','fullName']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description', 'pub_date', 'user_id', 'like_count', 'dislike_count','Q_id']

    # Make pub_date optional
    extra_kwargs = {'pub_date': {'required': False},
	'user_id': {'required': False}
	}
    def create(self, validated_data):
        # The 'user' field is already included in the validated_data
        return Question.objects.create(**validated_data)
# ------------------------------------------answer Serializer ------------------------------------------------
class AnswersSerializer(serializers.ModelSerializer):
    user = CustomUtilsUserSerializer(source='user_id', read_only=True)
    class Meta:
        model = Answers
        fields = ['Answer','pub_date','updated_date','user_id','Q_id','like_count','dislike_count','A_id','user']
    extra_kwargs = {'pub_date': {'required': False},
	'user_id': {'required': False}
	}   