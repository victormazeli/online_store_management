from django.shortcuts import render
from .models import CustomUser, UserInfo
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserInfoSerializer


# Create your views here.

class UserDetail(APIView):
    try:
        def get_object(self, pk):
            return CustomUser.objects.get(pk=pk)
    except user.DoesNotExist:
        raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserInfo(APIView):
    def get(self, request, pk, format=None):
        info = UserInfo.objects.filter(user_id=pk)
        serializer = UserInfoSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)
