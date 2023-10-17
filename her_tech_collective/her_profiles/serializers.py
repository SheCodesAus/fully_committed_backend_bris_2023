from rest_framework import serializers
from django.apps import apps
from .models import Location, Skills

class LocationSerializer(serializers.ModelSerializer):
    location=serializers.ReadOnlyField(source='location.id')
    class Meta:
        model = Location
        fields='__all__'

class SkillsSerializer(serializers.ModelSerializer):
    skills=serializers.ReadOnlyField(source='skills.id')

    class Meta:
        model = Skills        
        fields = '__all__'


class HerProfileSerializer(serializers.ModelSerializer):
    location=LocationSerializer(many=False, read_only=True)
    skills=SkillsSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('her_profiles.HerProfile')
        fields = '__all__'


