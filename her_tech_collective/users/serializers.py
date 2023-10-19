from rest_framework import serializers
from django.apps import apps
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('id', 'last_login', 'username','password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

    