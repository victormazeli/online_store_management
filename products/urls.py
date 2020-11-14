from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views
urlpatterns = [
    path('add_product/', views.AddProducts.as_view()),
    path('get_products/', views.StoreProducts.as_view()),
    path('product_detail/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_update/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_delete/<int:pk>/', views.StoreProductDetail.as_view()),
    path('get_images/<int:pk>/', views.ProductImages.as_view()),
    path('add_images/', views.ProductImages.as_view()),
    path('add_variation/', views.ProductVariation.as_view()),
    path('get_variation/<int:pk>/', views.ProductVariation.as_view()),
    path('add_options/', views.ProductOption.as_view()),
    path('get_options/<int:pk>/', views.ProductOption.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)