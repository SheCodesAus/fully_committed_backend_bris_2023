from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', views.HerProfileList.as_view()),
    # path('location', views.LocationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)