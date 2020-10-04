from django.shortcuts import render
from django.http import Http404
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Shop, Products, Category, Images, CustomerList
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer, ImageSerializer, CustomerListSerializer

# Create your views here.

class StoreCreation(APIView):##ensure to add permission class
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        store = Shop.objects.all()
        serializer = ShopSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreCustomersList(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop']
    def get(self, request, format=None):
        customer_list = CustomerList.objects.all()
        serializer = CustomerListSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CustomerListSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):##ensure to add permission class
    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        store_detail = self.get_object(pk)
        serializer = ShopSerializer(store_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = ShopSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreProducts(APIView):##ensure to add permission class
     parser_classes = [MultiPartParser]
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['shop', 'category']
     search_fields = ['name']
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# class ProductImageUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk) 
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class StorCategory(APIView):
    """
    docstring
    """
    def post(self, request, format=None):

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def get(self, request, format=None):
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
