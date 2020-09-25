from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from shop.models import Shop, Products
from .models import Order, OrderedItem, OrderStatus
from .serializers import OrderedItemSerializers, OrderSerializer, OrderStatusSerializer

# Create your views here.

class ProductOrdered(APIView):
    def get(self, request, pk, format=None):
        items_ordered = OrderedItem.objects.filter(products__shop=pk)
        serializer = OrderedItemSerializers(items_ordered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self, request, pk, format=None):
    #     pass

class CreateOrder(APIView):
    def post(self, request, format=True):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddItem(APIView):
    def post(self, request, format=True):
        serializer = OrderedItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersDetail(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=True):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=True):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderedItem.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=True):
        ordered_item = self.get_object(pk)
        serializer = OrderedItemSerializers(ordered_item, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=True):
        ordererd_item = self.get_object(pk)
        ordererd_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

