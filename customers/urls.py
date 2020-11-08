from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views
urlpatterns = [
    path('list/', views.StoreCustomersList.as_view()),
    path('cart_update/<int:pk>/', views.CustomerCartView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)