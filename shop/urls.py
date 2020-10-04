from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [
    path('get_all_store/', views.StoreCreation.as_view()),
    path('create_store/', views.StoreCreation.as_view()),
    path('store_detail/<int:pk>/', views.StoreDetail.as_view()),
    # path('customer_list/<int:pk>/', views.StoreCustomersList.as_view()),
    path('customer_list/', views.StoreCustomersList.as_view()),
    path('update_store/<int:pk>/', views.StoreDetail.as_view()),
    path('add_product/', views.StoreProducts.as_view()),
    path('add_category/', views.StoreCategory.as_view()),
    # path('product_image_upload/', views.ProductImageUpload.as_view()),
    # path('store_product/<int:pk>/', views.StoreProducts.as_view()),
    path('store_product/', views.StoreProducts.as_view()),
    path('product_detail/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_update/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_delete/<int:pk>/', views.StoreProductDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)