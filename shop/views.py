from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core import serializers
from .models import Shop, Domain
from customers.models import Customers, CustomerCart
from orders.models import Order
from users.models import CustomUser

##Storefront view

class HomePage(TemplateView):
  template_name = "shop/base.html"

# def collections(request):
#     return render(request)

# def cart_page(request):
#     return render(request)

# def checkout(request):
#     return render(request)

def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            data = Customers.objects.filter(email=email, password=password)
            ser_instance = serializers.serialize('json', [ data, ])
            return JsonResponse({'data':ser_instance}, status=200)
        except Customers.DoesNotExist:
            return JsonResponse({'error':'Invalid email or password'}, status=400)


def customer_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        customer = Customers.objects.get(email=email)
        if customer:
            return JsonResponse({'error':'customer already exist'}, status=401)
        else:
          ser_instance = serializers.serialize('json', [ customer,])
        return JsonResponse({'data':ser_instance}, status=201) 
    return JsonResponse({'error':'can not register user'}, status=400)
     
def addcart(request):
    if request.method == 'POST':
      cart = CustomerCart(request.POST)
      instance = cart.save()
      ser_instance = serializers.serialize('json', [ instance,])
      return JsonResponse({'data':ser_instance}, status=200)
    return JsonResponse({'error':'can not add to cart'}, status=400)

def deletecartitem(request):
    if request.method == 'POST':
      item_id = request.POST.get('item_id')
      cart_id = request.POST.get('cart_id')
      cart = CustomerCart.objects.get(pk=cart_id)
      cart.items.remove(item_id)
      instance = cart.save()
      ser_instance = serializers.serialize('json', [ instance,])
      return JsonResponse({'data':ser_instance}, status=200)
    return JsonResponse({'error':'can not remove item '}, status=400)

def cart_customer(request, pk):
  if request.method == 'GET':
    cart = CustomerCart.objects.filter(customer_id=pk)
    data = {
      'cart_id':cart.id,
      'items': [
        {
          'item_name': cart.items.name,
          'item_price': cart.items.price,
          'item_unit': cart.items.unit

        }
      ],
      'option': {
        'option': cart.item_option.option.option_name,
        'value':cart.item_option.value
      },

      'quantity': cart.qty,
      'total': cart.total,
    }
    return JsonResponse(data, status=200)
  return JsonResponse({'error': 'could not fetch products'}, status=400)

def create_order(request):
    if request.method == 'POST':
      new_order = Order(request.POST)
      instance = new_order.save()
      ser_instance = serializers.serialize('json', [ instance,])
      return JsonResponse({'data':ser_instance}, status=200)
    return JsonResponse({'error':'can not create order'}, status=400)

def registration(request):
    if request.method == 'POST':
           tenant_name = request.POST.get('name')
           user_id = request.POST.get('id')
           user = CustomUser.objects.get(pk=user_id)
           url = '.cyphertech.com.ng'
           tenant = Shop(name=tenant_name, schema_name=tenant_name, user=user)
           tenant.save()

           domain = Domain()
           domain.domain = tenant.name + url
           domain.tenant = tenant
           domain.is_primary = True
           domain_instance = domain.save()
           ser_fqdn = serializers.serialize('json', [ domain_instance, ])
           return JsonResponse({'data':ser_fqdn}, status=201)
    return JsonResponse({'error':'Error creating store'}, status=400)