from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin


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


# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):     #class-based “protected” view
    model = Recipe                                    #specify model
    template_name = 'recipes/recipes_list.html'               #specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):   #class-based “protected” view
    model = Recipe                                    #specify model
    template_name = 'recipes/recipes_detail.html'             #specify template