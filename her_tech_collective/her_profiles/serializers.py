from rest_framework import serializers
from django.apps import apps
from .models import HerProfile, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name')


class HerProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)
    class Meta:
        model = HerProfile
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location_obj = Location.objects.create(**location_data)
        herprofile = HerProfile.objects.create(location=location_obj, **validated_data)
        return herprofile



# class SkillsSerializer(serializers.ModelSerializer):
#     skills=serializers.ReadOnlyField(source='skills.id')

#     class Meta:
#         model = Skills        
#         fields = '__all__'


