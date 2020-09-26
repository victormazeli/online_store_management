from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Products

# Create your models here.


class CustomerCart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
class CustomerCartItem(models.Model):
    cart = models.ForeignKey(CustomerCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)