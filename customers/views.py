from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import CustomerCart, CustomerCartItem, CustomerList
from .serializers import CustomerCartSerializer, CustomerListSerializer, CustomerCartItemSerializer


class StoreCustomersList(APIView):
    def get(self, request, pk, format=None):
        customer_list = CustomerList.objects.filter(shop_id=pk)
        serializer = CustomerListSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        serializer = CustomerListSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerCartView(APIView):
    def post(self, request, format=None):
        serializer = CustomerCartSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerCartItemView(APIView):
    def get(self, request, pk, format=None):
        cart_item =  CustomerCartItem.objects.filter(cart_user=pk)
        serializer = CustomerCartItemSerializer(cart_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CustomerCartItemSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        cart_item = CustomerCartItem.objects.get(pk)
        serializer = CustomerCartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cart_item = CustomerCartItem.objects.get(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
