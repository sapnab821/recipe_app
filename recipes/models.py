from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Recipe(models.Model):
    # class attributes
    name = models.CharField(max_length=50)
    ingredients = models.CharField(
        max_length=225, help_text="Enter the ingredients, separated by a comma"
    )
    cooking_time = models.IntegerField(help_text="Enter cooking time in minutes")
    difficulty = None
   

# string representation
def __str__(self):
    return str(self.name)