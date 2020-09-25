from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [

    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('user_info/<int:pk>/', views.UserInfo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)