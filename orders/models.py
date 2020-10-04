from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Products

# Create your models here.

class OrderStatus(models.Model):
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.status

class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user.email

# class OrderedItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    

#     def __str__(self):
#         return self.products.name

 



