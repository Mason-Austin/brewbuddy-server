from django.db import models
from .user import User

class Brew(models.Model):

    """This is the model for brews in the app brew buddy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    stage = models.CharField(max_length=50, default='Not Started')
    image = models.ImageField(upload_to='brew_images/', blank=True, null=True)
