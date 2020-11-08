from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import CustomerCart, Customers
from products.models import Products, ProductImages, ProductVariation
from .serializers import CustomerCartSerializer, CustomerListSerializer

# Create your views here.
class StoreCustomersList(APIView):
    def get(self, request, format=None):
        customer_list = Customers.objects.all()
        serializer = CustomerListSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerCartView(APIView):
    def get_object(self, pk):
        try:
            return CustomerCart.objects.get(pk=pk)
        except CustomerCart.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CustomerCartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

