from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('register/', views.CustomUserList.as_view()),
    path('<int:pk>/', views.CustomUserDetail.as_view()),
    path('<str:username>/', views.CustomUserByUsername.as_view())
]