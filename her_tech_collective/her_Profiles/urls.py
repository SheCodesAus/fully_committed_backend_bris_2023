from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HerProfileList.as_view()),
    # path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    # path('pledges/', views.PledgeList.as_view()),
    # path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    # path('category/', views.CategoryList.as_view()),
    # path('idol/', views.IdolList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)