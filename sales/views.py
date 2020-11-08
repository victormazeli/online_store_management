from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Transaction
from orders.models import Order
from .serializers import TransactionSerializer
from orders.serializers import OrderSerializer

# Api your views here.    
  
class SalesView(APIView):
    def get(self, request, format=None):
        wallet = Order.objects.values('date_created').annotate(daily_sales=Sum('total_cost'))
        serializer = OrderSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionHistory(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['txn_date']
    def get(self, request, format=None):
        trxn = Transaction.objects.all()
        serializer = TransactionSerializer(trxn, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        trxn = Transaction.objects.get(pk=pk)
        trxn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


