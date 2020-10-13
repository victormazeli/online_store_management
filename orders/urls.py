from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from orders import views

urlpatterns = [

    path('store/orders/<int:pk>/', views.GetOrders.as_view()),
    path('store/create_order/', views.CreateOrder.as_view()),
    path('store/add_order_item/', views.AddItem.as_view()),
    path('store/delete_order/<int:pk>/', views.OrdersDetail.as_view()),
    path('store/order_by_status/<int:pk>/', views.OrderStatus.as_view()),
    # path('store/order_item_update/<int:pk>/', views.OrderItemDetail.as_view()),
    path('store/order_item_delete/<int:pk>/', views.OrderItemDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)