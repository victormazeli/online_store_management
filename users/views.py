from django.shortcuts import render
from django.http import Http404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from shop.models import Shop
from .serializers import UserSerializer, ShopSerializer
from tenant_users.tenants.tasks import provision_tenant


# Create your views here.


class Registration(APIView):##ensure to add permission class
    def post(self, request, format=None):
        marchant = CustomUser.objects.create_user(email=request.data['email'], password=request.data['password'])
        new_marchant = marchant.save()
        fdqn = provision_tenant(tenant_name=request.data['name'], tenant_slug=request.data['slug'], user_email=request.data['email'])
        ser_instance = serializers.serialize('json', [new_marchant])
        return Response(data={'marchant':ser_instance, 'Fqdn':fdqn}, status=status.HTTP_201_CREATED)


class StoreDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'id']

    try:
        def get_object(self, pk):
            return Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        raise Http404

    def get(self, request, format=None):
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    try:
        def get_object(self, pk):
            return CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
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


