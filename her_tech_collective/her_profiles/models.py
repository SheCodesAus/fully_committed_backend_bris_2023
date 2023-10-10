from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

class Location(models.Model):
    location_name = models.CharField(max_length=200, null=True) 
    location_slug = models.SlugField(unique=True) 

class Skills(models.Model):
    skill_name = models.CharField(max_length=200, null=True) 
    skill_slug = models.SlugField(unique=True)

class HerProfile(models.Model):
    profile_name = models.CharField(max_length=200, null=True) 
    job_title = models.TextField()
    linkedin_url = models.URLField()
    image_url = models.URLField()
    bio = models.TextField()
    is_active = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, null=True)
    skills = models.ForeignKey(
        Skills, 
        on_delete=models.CASCADE, null=True)
    owner = models.CharField(max_length=200, null=True)

    
Hello