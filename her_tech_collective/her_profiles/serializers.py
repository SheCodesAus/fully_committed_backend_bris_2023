from rest_framework import serializers
from django.apps import apps
from .models import HerProfile, Location, Skills
from users.serializers import CustomUserSerializer

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name')

class SkillsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
            return {
                "id": instance.id,
                "skill_name": instance.skill_name
            }

    def to_internal_value(self, data):
            id = data.get("id")
            skill_name = data.get("skill_name")
            if not id:
                raise serializers.ValidationError("id is required")
            if not skill_name:
                raise serializers.ValidationError("skill_name is required")
            return Skills(id=id, skill_name=skill_name)

    class Meta:
        model = Skills
        fields = '__all__'

class HerProfileSerializer(serializers.ModelSerializer):
    location=LocationSerializer(many=False)
    skills=SkillsSerializer(many=True)
    # skills = serializers.PrimaryKeyRelatedField(many=True, queryset=Skills.objects.all())
    # owner = serializers.ReadOnlyField(source='owner.id') 
    # read_only=True
    owner = CustomUserSerializer(read_only=True) 

    class Meta:
        model = HerProfile
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        skills_data = validated_data.pop("skills")
        location = Location.objects.create(**location_data) 
        herprofile = HerProfile.objects.create(location=location, **validated_data) 
        for skill_data in skills_data:
            # unpacking
            skill_dict = {"id": skill_data.id, "skill_name": skill_data.skill_name}
            skill, created = Skills.objects.get_or_create(**skill_dict) 
            herprofile.skills.add(skill) 
        return herprofile

    def update(self, instance, validated_data):
        location_data = validated_data.pop("location", None)
        skills_data = validated_data.pop("skills", None)
        if location_data:
            location = Location.objects.create(**location_data) 
            setattr(instance, "location", location) 
        if skills_data:
            instance.skills.clear() # Clear the existing skills of the HerProfile instance
            for skill_data in skills_data:
                skill_dict = {"id": skill_data.id, "skill_name": skill_data.skill_name}
                skill, created = Skills.objects.get_or_create(**skill_dict) 
                instance.skills.add(skill)
        # instance.profile_name = validated_data['']
        # print('validated_data', validated_data)
        # print('instance', instance.job_title)
        instance.job_title = validated_data['job_title']
        instance.profile_name = validated_data['profile_name']
        instance.linkedin_url=validated_data['linkedin_url']
        instance.image_url=validated_data['image_url']
        instance.bio=validated_data['bio']
        instance.is_active=validated_data['is_active']
        instance.save() 
        return instance

