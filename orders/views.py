
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class Orders(APIView):
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['status', 'id']
     def get(self, request, format=True):
        ordereditems = Order.objects.all()
        serializer = OrderSerializer(ordereditems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    
class OrdersDetail(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=True):
        items = self.get_object(pk)
        ordereditems = Order.objects.filter(pk=items.id)
        serializer = OrderSerializer(ordereditems)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def delete(self, request, pk, format=True):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

