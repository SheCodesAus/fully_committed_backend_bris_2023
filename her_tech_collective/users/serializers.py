from rest_framework import serializers
from django.apps import apps
from .models import CustomUser

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'