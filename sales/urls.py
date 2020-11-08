from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sales import views
urlpatterns = [
    path('sales/', views.SalesView.as_view()),
    path('get_transactions/', views.TransactionHistory.as_view()),
    path('delete_transactions/<int:pk>/', views.TransactionHistory.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)