from rest_framework import serializers
from django.apps import apps
from .models import Location
# from django.contrib.auth import get_user_model

class LocationSerializer(serializers.ModelSerializer):
    location=serializers.ReadOnlyField(source='location.id')
    class Meta:
        model = Location
        fields='__all__'

class HerProfileSerializer(serializers.ModelSerializer):
    # owner=OwnerSerializer(many=False, read_only=True)
    
    class Meta:
        model = apps.get_model('her_profiles.HerProfile')
        fields = '__all__'
        # fields = ['profile_name', 'job_title', 
        #     'linkedin_url', 'image_url', 'bio', 'is_active', 
        #     'date_created', 'lcoation', 'skills', 'owner']



# class SkillsSerializer(serializers.ModelSerializer):
#     skills=serializers.ReadOnlyField(source='skills.id')

    # class Meta:
    #     model = Skills        
    #     fields = '__all__'

# class OwnerSerializer(serializers.ModelSerializer):
#     # owner=serializers.ReadOnlyField(source='owner.id')

#     class Meta:
#         model = get_user_model()      
#         fields = '__all__'
#         # ('id', 'username', 'email')



# class HerProfileSerializer(HerProfileSerializer):
#     location=LocationSerializer(many=False, read_only=True)
#     skills=SkillsSerializer(many=True, read_only=True)
#     owner=OwnerSerializer(many=False, read_only=True)

