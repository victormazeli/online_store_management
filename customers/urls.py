from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views

urlpatterns = [
    path('cutsomer_list/<int:pk>/', views.StoreCustomersList.as_view()),
    path('cutsomer_register/', views.StoreCustomersList.as_view()),
    path('cutsomer_cart_add/', views.CustomerCartView.as_view()),
    path('cutsomer_cart_item/<int:pk>/', views.CustomerCartItemView.as_view()),
    path('cutsomer_cart_item_add/', views.CustomerCartItemView.as_view()),
    path('cutsomer_cart_item_update/<int:pk>', views.CustomerCartItemView.as_view()),
    path('cutsomer_cart_item_delete/<int:pk>', views.CustomerCartItemView.as_view()),
 

]

urlpatterns = format_suffix_patterns(urlpatterns)