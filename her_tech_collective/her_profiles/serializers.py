from rest_framework import serializers
from django.apps import apps
from .models import HerProfile, Location, Skills

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name')

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"

class HerProfileSerializer(serializers.ModelSerializer):
    location=LocationSerializer(many=False)
    skills = serializers.PrimaryKeyRelatedField(many=True, queryset=Skills.objects.all())
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = HerProfile
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        skills_data = validated_data.pop('skills')
        location = Location.objects.create(**location_data)
        herprofile = HerProfile.objects.create(location=location, **validated_data)
        herprofile.skills.set(skills_data)
        return herprofile


    # def update(self, instance, validated_data):
    #     location_data = validated_data.pop('location')
    #     skills_data = validated_data.pop('skills')
    #     instance.location.update(**location_data)
    #     instance.update(**validated_data)
    #     instance.skills.set(skills)
    #     return instance



