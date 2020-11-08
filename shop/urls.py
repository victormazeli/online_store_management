from django.urls import path, include
from shop import views

urlpatterns = [
    path('add/', views.addcart, name='addcart'),
    path('delete/item/', views.deletecartitem, name='deleteitem'),
    path('create/', views.create_order, name='create_order'),
    
]