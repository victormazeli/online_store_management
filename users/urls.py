from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('registration/', views.Registration.as_view()),
    path('get_store/', views.StoreDetail.as_view()),
    path('update_store/', views.StoreUpdate.as_view()),
    path('user_update/', views.UserUpdate.as_view()),
    path('user_detail/', views.UserDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)