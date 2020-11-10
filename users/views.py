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
from shop.models import Shop, Domain
from .serializers import UserSerializer, ShopSerializer, DomainSerializer


# Create your views here.

class Registration(APIView):##ensure to add permission class
    def post(self, request, format=None):
       try:
           tenant = Shop(name=request.data['name'], schema_name=request.data['name'])
           tenant.save()

           domain = Domain()
           domain.domain = request.data['name'] + '.cyphertech.com.ng'
           domain.tenant = tenant
           domain.is_primary = True
           domain.save()
           data = {'store_id':tenant.id, 'store_url':domain.domain}
       except Shop.DoesNotExist or Domain.DoesNotExist:
           return Response(data={'error':'Error creating store'}, status=status.HTTP_400_BAD_REQUEST)
       return Response(data=data, status=status.HTTP_201_CREATED)
        
        

class StoreDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user']

    def get(self, request, format=None):
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class StoreUpdate(APIView):
    parser_classes = [MultiPartParser]

    try:
        def get_object(self, pk):
            return Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        raise Http404
    
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


