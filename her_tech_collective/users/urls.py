from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('register/', views.CustomUserCreate.as_view()),
    path('account/<int:pk>/', views.CustomUserDetail.as_view()),
]