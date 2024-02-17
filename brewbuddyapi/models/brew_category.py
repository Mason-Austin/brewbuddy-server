from django.db import models
from .category import Category
from .brew import Brew

class BrewCategory(models.Model):

    """This is the model for the join table between brew and category"""
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE, related_name = 'categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brews')
