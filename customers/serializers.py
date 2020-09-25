from rest_framework import serializers
from .models import CustomerCart, CustomerCartItem, CustomerList


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomerList
      field = '__all__'

class CustomerCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCartItem
        field = '__all__'

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomerList
      field = '__all__'