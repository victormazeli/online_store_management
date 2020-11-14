from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from products.models import Products, ProductImages, ProductVariation
from .serializers import ProductSerializer, ProductImagesSerializer, ProductVariationSerializer, ProductOptionSerializer

# Api your views here.    

class StoreProducts(APIView):##ensure to add permission class
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['id', 'name']
     def get(self, request, format=None):
         products = Products.objects.all().order_by('-id')
         serializer = ProductSerializer(products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)


class AddProducts(APIView):##ensure to add permission class
     def post(self, request, format=None):
         serializer = ProductSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductImages(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request, pk, format=None):
        images = ProductImages.objects.filter(product=pk)
        serializer = ProductImagesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductImagesSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductVariation(APIView):
    def get(self, request, pk, format=None):
        variation = ProductVariation.objects.filter(product=pk)
        serializer = ProductVariationSerializer(variation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductVariationSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductOption(APIView):
    def get(self, request, pk, format=None):
        option = ProductOption.objects.filter(product=pk)
        serializer = ProductOptionSerializer(option, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductOptionSerializer(data=request.data)
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




    

# def products(request):
#     if request.method == 'GET':
#         product = Products.objects.all()
#         data = {
#             'product_name':product.name, 
#             'product_description':product.description,
#             'product_price':product.price,
#             'quantity': product.quantity_in_stock,
#             'extra_details':product.extra_detail,
#             'product_images': [
#                 {
#                     'images': product.images.image
#                 }
#                 ],
#             'options': {
#                 'option':product.options.option.option_name,
#                 'value':product.options.values,
#                 'price':product.options.price,
#                 'quantity':product.options.quantity
#             }

#             }

#         return JsonResponse(data, status=200)
#     return JsonResponse({'error': 'could not fetch products'}, status=400)


# def limit_products(request, page):
#     if request.method == 'GET':
#         product = Products.objects.all()[:page]
#         data = {
#             'product_name':product.name, 
#             'product_description':product.description,
#             'product_price':product.price,
#             'quantity': product.quantity_in_stock,
#             'extra_details':product.extra_detail,
#             'product_images': [
#                 {
#                     'images':product.images.image 
#                 }

#                 ],
#             'options': {
#                 'option':product.options.option.option_name,
#                 'value':product.options.values,
#                 'price':product.options.price,
#                 'quantity':product.options.quantity
#             }

#             }

#         return JsonResponse(data, status=200)
#     return JsonResponse({'error': 'could not fetch products'}, status=400)

# def fetch_product(request, pk):
#     if request.method == 'GET':
#         product = Products.objects.get(pk=pk)
#         data = {
#             'product_name':product.name, 
#             'product_description':product.description,
#             'product_price':product.price,
#             'quantity': product.quantity_in_stock,
#             'extra_details':product.extra_detail,
#             'product_images': [
#                 {
#                     'images':product.images.image
#                 }
#             ],
#             'options': {
#                 'option':product.options.option.option_name,
#                 'value':product.options.values,
#                 'price':product.options.price,
#                 'quantity':product.options.quantity
#             }

#             }

#         return JsonResponse(data, status=200)
#     return JsonResponse({'error': 'could not fetch products'}, status=400)