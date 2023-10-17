from django.contrib import admin
from django.urls import path
from django.urls import path, include
from her_profiles import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('her_profiles.urls')),
    path('profiles/<int:pk>/', views.HerProfileDetail.as_view()),
    path('account/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('location/', views.LocationList.as_view()),
    path('skills/', views.SkillsList.as_view()),
]
