from .models import CustomUser, UserInfo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomUser
      fields = ['email', 'is_marchant', 'date_joined']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
      model = UserInfo
      fields = '__all__'