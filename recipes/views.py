from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm, RecipeForm
import pandas as pd
from .utils import get_chart
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required


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
    template_name = 'recipes/recipes_list.html'  
 


class RecipeDetailView(LoginRequiredMixin, DetailView):   #class-based “protected” view
    model = Recipe                                    #specify model
    template_name = 'recipes/recipes_detail.html'
                 #specify template

def about(request):
    return render(request, 'recipes/about.html')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')  # Redirect to recipe list or any other page
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def records(request):

    form = RecipeSearchForm(request.POST or None)
    
    name_df = None
    chart = None

    if request.method == 'POST' and form.is_valid():
        search_term = request.POST.get('search_term', '').strip()
        chart_type = request.POST.get('chart_type', '')

        # Filter recipes based on the search term for the table
        qs_filtered = Recipe.objects.filter(
            Q(name__icontains=search_term) |
            Q(ingredients__icontains=search_term) |
            Q(cooking_time__icontains=search_term)
        )


        # Create DataFrame for filtered recipes
        if qs_filtered.exists():
            name_df = pd.DataFrame(qs_filtered.values())
            name_df['ingredient_count'] = name_df['ingredients'].apply(lambda x: len(x.split(',')))
            name_df['link'] = name_df['id'].apply(lambda x: f'<a href="{reverse("recipes:detail", args=[x])}">Recipe Details</a>')
            # Add image tags
            name_df['pic'] = name_df['pic'].apply(lambda x: f'<img src="/media/{x}" width="100" height="100"/>')

           
            chart = get_chart(chart_type, name_df)
            name_df = name_df.to_html(escape=False)
            
        else:
            name_df = "<p>No recipes found.</p>"

        # Generate the chart using all recipes
        

    context = {
        'form': form,
        'name_df': name_df,
        'chart': chart
    }
    
   

    
    # Load the recipes/records.html page using the data that you just prepared
    return render(request, 'recipes/records.html', context)



