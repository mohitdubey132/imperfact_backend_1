import uuid
import bcrypt  # Import bcrypt

from django.db import models
from enum import Enum
from django.contrib.auth import authenticate

class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'
    EXPERT = 'expert'
    SPECIAL_PERSON = 'special_person'

class CustomUser(models.Model):
    U_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userType = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in UserType], default=UserType.USER.value)
    fullName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    userName = models.CharField(max_length=255, unique=True, null=True)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    mobileNo = models.CharField(max_length=10)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.fullName

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Automatically updated on each save
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to link with the User model
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    Q_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.title

class Answers(models.Model):
    Answer = models.CharField(max_length=255)
    # description = models.TextField()
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Automatically updated on each save
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to link with the User model
    Q_id = models.ForeignKey(Question, on_delete=models.CASCADE) 
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    A_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.Answer