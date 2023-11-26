from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['U_id', 'userType', 'userName','fullName','password', 'age', 'gender', 'address', 'mobileNo', 'country']
