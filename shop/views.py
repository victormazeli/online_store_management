from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView
from django.core import serializers
from .models import Shop, Domain
from customers.models import Customers, CustomerCart
from orders.models import Order
from users.models import CustomUser

##Storefront view

def index(request):
    domain = Domain.objects.get(tenant=request.tenant)
    try:
      store = Shop.objects.get(pk=domain.tenant)
    except Shop.DoesNotExist:
        raise Http404("Store does not exist")
    return render(request, 'shop/base.html', {'store_detail': store } )


# def collections(request):
#     return render(request)

# def cart_page(request):
#     return render(request)

# def checkout(request):
#     return render(request)


