from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
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

    def post(self, request, format=None):
        serializer = CustomerCartSerializer(request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CustomerCartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=True):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerCartDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['items', 'id', 'customer']
    def get(self, request, format=None):
        cart = CustomerCart.objects.all()
        serializer = CustomerCartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Signup(APIView):
    def post(self, request, format=None):
        try:
            email = request.data['email']
            Customers.objects.get(email=email)
        except Customers.DoesNotExist:
            serializer = CustomerCartSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error':'User Already registered'}, status=400) 

class Login(APIView):
    def post(self, request, format=None):
        try:
            email = request.data['email']
            password = request.data['password']
            Customers.objects.filter(email=email, password=password)
        except Customers.DoesNotExist:
            return JsonResponse({'error':'invalid credentials'}, status=400 )
        return JsonResponse({'success':'valid credentials'}, status=200 ) 