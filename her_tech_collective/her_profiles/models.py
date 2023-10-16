from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

# class Skills(models.Model):
#     skill_name = models.CharField(max_length=200, null=True) 
#     skill_slug = models.SlugField(unique=True)

#     def __str__(self) -> str:
#         return f'{self.skill_name, self.skill_slug}'

class Location(models.Model):
    location_name = models.CharField(max_length=200, null=True) 
    # location_slug = models.SlugField(unique=True)
    
    def __str__(self) -> str:
        return f'{self.location_name}'

class HerProfile(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True)
    profile_name = models.CharField(max_length=200, null=True) 
    job_title = models.TextField()
    linkedin_url = models.URLField()
    image_url = models.URLField()
    bio = models.TextField()
    is_active = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now)
    skills = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=200, null=True)

    
# related_name='location_herprofiles', 

    # l
    # skills = models.ManyToManyField(Skills)