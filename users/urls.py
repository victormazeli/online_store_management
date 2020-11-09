from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [

    # path('get_user/<int:pk>/', views.UserDetail.as_view()),
    # path('update/<int:pk>/', views.UserDetail.as_view()),
    path('registration/', views.Registration.as_view()),
    path('get_store/', views.StoreDetail.as_view()),
    path('update_store/', views.StoreDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)