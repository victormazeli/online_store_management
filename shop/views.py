from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView
from django.core import serializers
from .models import Shop, Domain
from customers.models import Customers, CustomerCart
from orders.models import Order
from users.models import CustomUser
from products.models import Products

##Storefront view

def index(request):
    domain = Domain.objects.get(tenant=request.tenant)
    products = Products.objects.all()[:10]
    try:
      store = Shop.objects.get(pk=domain.tenant)
    except Shop.DoesNotExist:
        raise Http404("Store does not exist")
    return render(request, 'shop/index.html', {'store_detail': store, 'products':products} )


# def collections(request):
#     return render(request)

# def cart_page(request):
#     return render(request)

# def checkout(request):
#     return render(request)

def limit_products(request, page):
    if request.method == 'GET':
        product = Products.objects.all()[:page]
        data = {
            'product_name':product.name, 
            'product_description':product.description,
            'product_price':product.price,
            'quantity': product.quantity_in_stock,
            'extra_details':product.extra_detail,
            'product_images': [product.images.image],
            'options': [
                {
                'option':product.options.option.option_name,
                'value':product.options.values,
                'price':product.options.price,
                'quantity':product.options.quantity
                }
            ]

            }

        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'could not fetch products'}, status=400)
