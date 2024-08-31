from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart
from django.shortcuts import reverse


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
    template_name = 'recipes/recipes_detail.html'             #specify template

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
            Q(ingredients__icontains=search_term)
        )

        # Get all recipes for the graph
        qs_all = Recipe.objects.all()

        # Create DataFrame for filtered recipes
        if qs_filtered.exists():
            name_df = pd.DataFrame(qs_filtered.values())
            name_df['ingredient_count'] = name_df['ingredients'].apply(lambda x: len(x.split(',')))
            name_df['link'] = name_df['id'].apply(lambda x: f'<a href="{reverse("recipes:detail", args=[x])}">Recipe Details</a>')
            # Add image tags
            name_df['pic'] = name_df['pic'].apply(lambda x: f'<img src="/media/{x}" width="100" height="100"/>')

            name_df = name_df.to_html(escape=False)
        else:
            name_df = "<p>No recipes found.</p>"

        # Create DataFrame for all recipes for the graph
        df_all = pd.DataFrame(qs_all.values())
        df_all['ingredient_count'] = df_all['ingredients'].apply(lambda x: len(x.split(',')))
 

        # Generate the chart using all recipes
        chart = get_chart(chart_type, df_all)

    context = {
        'form': form,
        'name_df': name_df,
        'chart': chart
    }
    
   

    
    # Load the recipes/records.html page using the data that you just prepared
    return render(request, 'recipes/records.html', context)




'''
from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe
from django.db.models import Q
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from django.shortcuts import render



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
    template_name = 'recipes/recipes_detail.html'             #specify template


#define function-based view - records()
def records(request):
    #create an instance of IngredientSearchForm that you defined in recipe/forms.py
    form = RecipeSearchForm(request.POST or None)

  
    name_df= None
    chart = None

   #check if the button is clicked
    if request.method =='POST':
       #read book_title and chart_type
        name = request.POST.get('name','ingredients')
        chart_type = request.POST.get('chart_type')
        # Apply filter to extract data
        qs = Recipe.objects.filter(Q(name=name) | Q(ingredients=name))
        if qs:      #if data found
           #convert the queryset values to pandas dataframe
           name_df=pd.DataFrame(qs.values()) 
        print (name, chart_type)


        name_df=name_df.to_html()

        print ('Exploring querysets:')
        print ('Case 1: Output of Sale.objects.all()')
        qs=Recipe.objects.all()
        print (qs)

        print ('Case 2: Output of Sale.objects.filter(ingredient=ingredients)')
        qs =Recipe.objects.filter(name=name)
        print (qs)

        print ('Case 3: Output of qs.values')
        print (qs.values())

        print ('Case 4: Output of qs.values_list()')
        print (qs.values_list())

        print ('Case 5: Output of Recipe.objects.get(id=1)')
        obj = Recipe.objects.get(id=1)
        print (obj)

       
   #pack up data to be sent to template in the context dictionary
    context={
           'form': form,
           'recipe_df': name_df,
           'chart': chart
   }
   
   #load the recipes/record.html page using the data that you just prepared
    return render(request, 'recipes/records.html', context)
    '''