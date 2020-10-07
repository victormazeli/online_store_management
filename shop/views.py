from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.http import Http404
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Shop, Products, Category, CustomerList, Domain
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer, CustomerListSerializer, DomainSerializer

# Api your views here.

class StoreCreation(APIView):##ensure to add permission class
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        store = Shop.objects.all()
        serializer = ShopSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDomainCreation(APIView):##ensure to add permission class
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        store = Domain.objects.get(tenant=pk)
        serializer = DomainSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreCustomersList(APIView):
    def get(self, request, pk, format=None):
        customer_list = CustomerList.objects.filter(shop=pk)
        serializer = CustomerListSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CustomerListSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):##ensure to add permission class
    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        store_detail = self.get_object(pk)
        serializer = ShopSerializer(store_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = ShopSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreProducts(APIView):##ensure to add permission class
     parser_classes = [MultiPartParser]
     def get(self, request, pk, format=None):
         products = Products.objects.filter(shop=pk)
         serializer = ProductSerializer(products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
    
     def post(self, request, format=None):
         serializer = ProductSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# class ProductImageUpload(APIView):
    # parser_classes = [MultiPartParser]
    # def post(self, request, format=None):
    #     serializer = ImageSerializer(data=request.data)
    #     if serializer.is_valid():
    #       serializer.save()
    #       return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk) 
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class StoreCategory(APIView):

    def post(self, request, format=None):

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def get(self, request, format=None):
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


##Storefront view code snippets

class Home(TemplateView):
    """
    Store Home page
    """
    template_name = 'shop/index_shop.html'

    def get_context_data(self, **Kwargs):
        context = super().get_context_data(**Kwargs)
        domain = Domain.objects.get(tenant=self.request.tenant)
        context['store'] = domain
        context['store_products'] = Products.objects.filter(shop=domain.tenant)[:5]
        return context    


class StoreProduct(ListView):
    """
    Store products
    """
    template_name = 'shop/shop_product_col_4.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.domain = get_object_or_404(Domain, tenant=self.request.tenant)
        return Products.objects.filter(shop=self.domain.tenant)

class ProductDetail(DetailView):
    """
    product detail
    """
    queryset = Products.objects.all()
    context_object_name = 'product_detail'
    template_name = 'shop/shop_single_product.html'

def signup_view(request):
    if request.method == 'POST':
        shop = Shop.objects.get(tenant=request.tenant)
        customer = CustomerList()
        form1 = SignUpForm(request.POST)
        if form1.is_valid():
                user= form1.save()
                user.email = form1.cleaned_data.get('email')
                user.password1 = form1.cleaned_data.get('password1')
                user.is_marchant = True
                user.save()
                customer.user = user.id
                customer.shop = shop.id
                customer.save()
        return redirect('login') 
    else:
        form =SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST': 
        email = request.POST['email']
        password = request.POST['password1']
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
         return redirect('sign-up')
    else:
        form =LoginForm()
        return render(request, 'registration/login_register.html', {'form': form})



# class CustomerCart():
#     """
#     docstring
#     """
#     pass

# class CustomerCartDetail():
#     """
#     docstring
#     """
#     pass

# class CustomerOrder():
#     """
#     docstring
#     """
#     pass

# class CustomerOrderDetail():
#     """
#     docstring
#     """
#     pass