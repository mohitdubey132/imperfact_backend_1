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

    # def save(self, *args, **kwargs):
        # Hash the password using bcrypt before saving
        # if self._state.adding:  # Check if it's a new object (not an update)
        #     self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        # super().save(*args, **kwargs)

    # def authenticate_user(self, password):
        # Authenticate the user
        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8'))

        # if bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')):
            # Authentication successful
            # return self
        # else:
            # Authentication failed
            # return None

    def __str__(self):
        return self.fullName
