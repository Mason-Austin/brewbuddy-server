from django.db import models

class User(models.Model):
  
    """This is the model for users in the app BrewBuddy"""
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True)
