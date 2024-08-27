from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

class RecipeListView(ListView):                   #class-based view
   model = Recipe                             #specify model
   template_name = 'recipes/recipes_list.html'    #specify template 
   context_object_name = 'recipes'  # The context name in the template

class RecipeDetailView(DetailView):                       #class-based view
   model = Recipe                                       #specify model
   template_name = 'recipes/recipes_detail.html'                 #specify template