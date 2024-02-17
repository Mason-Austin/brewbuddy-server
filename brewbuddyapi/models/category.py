from django.db import models

class Category(models.Model):
  
    """This is the model for categories"""
    label = models.CharField(max_length=25)
    