from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    #add custom fields here

    def __str__(self):
        return self.username
    
    def create_user(self, email, password=None):
        '''
        Creates and saves a User with given email address
        '''

    user = self.,o

