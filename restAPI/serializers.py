from rest_framework import serializers
from .models import CustomUser ,Question , Answers

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['U_id', 'userType','password','userName','fullName', 'age', 'gender', 'address', 'mobileNo', 'country']
        
# class QuestionSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Question
# 		fields =['Q_id','title','description','pub_date','updated_date','like_count','dislike_count']
# 	# Make pub_date optional
#     extra_kwargs = {'pub_date': {'required': False}}

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

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['Answer','pub_date','updated_date','user_id','Q_id','like_count','dislike_count','A_id']
    extra_kwargs = {'pub_date': {'required': False},
	'user_id': {'required': False}
	}   