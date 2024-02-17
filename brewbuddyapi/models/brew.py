from django.db import models
from .user import User

class Brew(models.Model):

    """This is the model for brews in the app brew buddy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
