from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views

urlpatterns = [
    path('customer_cart_add/', views.CustomerCartView.as_view()),
    path('customer_cart_delete/<int:pk>/', views.CustomerCartView.as_view()),
    path('customer_cart_item/<int:pk>/', views.CustomerCartItemView.as_view()),
    path('customer_cart_item_add/', views.CustomerCartItemView.as_view()),
    path('customer_cart_item_delete/<int:pk>/', views.CustomerCartItemView.as_view()),
 

]

urlpatterns = format_suffix_patterns(urlpatterns)