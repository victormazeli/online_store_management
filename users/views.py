from django.shortcuts import render
from django.http import Http404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from shop.models import Shop
from .serializers import UserSerializer, ShopSerializer, DomainSerializer


# Create your views here.

class Registration(APIView):##ensure to add permission class
    parser_classes = [MultiPartParser]
    def post(self, request, format=None):
        data = {
           'name':request.data['name'], 
           'logo':request.data['logo'], 
           'description':request.data['description'], 
           'tagline':request.data['tagline'], 
           'schema_name':request.data['schema_name'] 
           }
        domain_data = {'domain':request.data['name'] + ".cyphertech.com.ng", 'is_primary':True}
        shop_serializer = ShopSerializer(data=data)
        domain_serializer = DomainSerializer(data=domain_data)
        if shop_serializer.is_valid() and domain_serializer.is_valid():
          shop_serializer.save()
          domain_serializer.save()
          return Response(data={'shop':shop_serializer.data, 'url':domain_serializer}, status=status.HTTP_201_CREATED)
        return Response(data={'shop_error':shop_serializer.errors, 'domain':domain_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'id', 'user']

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


# class UserDetail(APIView):
#     try:
#         def get_object(self, pk):
#             return CustomUser.objects.get(pk=pk)
#     except CustomUser.DoesNotExist:
#         raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


