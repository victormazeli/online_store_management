from django.urls import path
from orders import views

urlpatterns = [
 
    path('list/order/', views.Orders.as_view()),
    path('details/order/<int:pk>/', views.OrdersDetail.as_view()),
    path('delete/order/<int:pk>/', views.OrdersDetail.as_view()),
    path('create/order/', views.Createorders.as_view()),
  
]
