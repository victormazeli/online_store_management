from rest_framework import serializers
from .models import Customers, CustomerCart

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
      model = Customers
      fields = ['first_name', 'last_name', 'email', 'phone_no']


class CustomerCartSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomerCart
      fields = '__all__'
