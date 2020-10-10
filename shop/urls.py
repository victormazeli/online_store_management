from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Sign_up', views.signup_view, name='sign-up'),
    path('login', views.signup_view, name='login'),
    path('products/', views.StoreProduct.as_view(), name='product-list'),
    path('products_detail/<int:pk/', views.ProductDetail.as_view(), name='product-detail'),

    path('get_all_store/', views.StoreCreation.as_view()),
    path('create_store/', views.StoreCreation.as_view()),
    path('get_store_domain/<int:pk>/', views.StoreDomainCreation.as_view()),
    path('create_store_domain/', views.StoreDomainCreation.as_view()),
    path('store_detail/<int:pk>/', views.StoreDetail.as_view()),
    path('customer_list/<int:pk>/', views.StoreCustomersList.as_view()),
    path('update_store/<int:pk>/', views.StoreDetail.as_view()),
    path('add_product/', views.StoreProducts.as_view()),
    path('add_category/', views.StoreCategory.as_view()),
    path('get_categories/', views.StoreCategory.as_view()),
    path('products_by_category/<name>/', views.StoreCategory.as_view()),
    # path('product_image_upload/', views.ProductImageUpload.as_view()),
    path('store_product/<int:pk>/', views.StoreProducts.as_view()),
    path('product_detail/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_update/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_delete/<int:pk>/', views.StoreProductDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)