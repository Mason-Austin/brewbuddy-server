from django.db import models
from .brew import Brew

class BrewLog(models.Model):
  
  """This is the model for brew logs"""
  brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
  log = models.TextField()
  date = models.DateField()
