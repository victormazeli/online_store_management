from django.shortcuts import render, reverse
from django.db import models
from django.contrib.auth import get_user_model
# from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase


# Create your models here.

class Shop(TenantBase):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='profile_pic')
    description = models.CharField(max_length=256, null=True, blank=True)
    tagline = models.CharField(max_length=256, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True) #give a default date value
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    auto_create_schema = True

    def __str__(self):
        return self.name

    
# class Domain(DomainMixin):
#     pass

   
