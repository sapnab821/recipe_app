from django.db import models
from django.shortcuts import reverse


# Create your models here.



class Recipe(models.Model):
    # class attributes
    ingredients = models.CharField(
        max_length=225, help_text="Enter the ingredients, separated by a comma"
    )
    cooking_time = models.IntegerField(help_text="Enter cooking time in minutes")
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="recipes", default='no_picture.jpg')

    def difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(',')) < 4:
            return 'easy'
        elif self.cooking_time < 10 and len(self.ingredients.split(',')) >= 4:
            return 'medium'
        elif self.cooking_time >= 10 and len(self.ingredients.split(',')) < 4:
            return 'intermediate'
        elif self.cooking_time >=10 and len(self.ingredients.split(',')) >=4:
            return 'hard'

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    # string representation
    def __str__(self):
        return str(self.name)