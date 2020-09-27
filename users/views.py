from django.shortcuts import render
from .models import CustomUser, UserInfo
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserInfoSerializer


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({

        'user_profile': reverse('user-profile', request=request, format=format)
    })

# class UserDetail(APIView):
    try:
        def get_object(self, pk):
            return CustomUser.objects.get(pk=pk)
    except user.DoesNotExist:
        raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileInfo(APIView):
        try:
            def get_object(self, pk):
                return UserInfo.objects.get(user_id=pk)
        except user.DoesNotExist:
            raise Http404
        
        def get(self, request, pk, format=None):
            info = self.get_object(pk)
            serializer = UserInfoSerializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        def post(self, request, format=None):
            serializer = UserInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        def put(self, request, pk, format=None):
            user_info = self.get_object(pk)
            serializer = UserInfoSerializer(user_info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


