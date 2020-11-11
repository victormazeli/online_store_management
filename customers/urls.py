from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views
urlpatterns = [
    path('login/', views.Login.as_view()),
    path('signup/', views.Signup.as_view()),
    path('customers/list/', views.StoreCustomersList.as_view()),
    path('cart/list/', views.CustomerCartDetail.as_view()),
    path('cart/update/<int:pk>/', views.CustomerCartView.as_view()),
    path('cart/add/', views.CustomerCartView.as_view()),
    path('cart/delete/<int:pk>/', views.CustomerCartView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)