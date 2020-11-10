from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    
    path('get_store/', views.StoreDetail.as_view()),
    path('update_store/', views.StoreUpdate.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)