from django.urls import path
from orders import views

urlpatterns = [
    
    path('list/', views.Orders.as_view()),
    path('details/<int:pk>/', views.OrdersDetail.as_view()),
    path('delete/<int:pk>/', views.OrdersDetail.as_view()),
  
]
