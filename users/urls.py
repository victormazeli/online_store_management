from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [

    # path('get_user/<int:pk>/', views.UserDetail.as_view()),
    # path('update/<int:pk>/', views.UserDetail.as_view()),
    # path('user_info/<int:pk>/', views.ProfileInfo.as_view()),
    # path('user_info/update/<int:pk>/', views.ProfileInfo.as_view()),
    # path('user_info/create/', views.ProfileInfo.as_view(), name='user-profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)