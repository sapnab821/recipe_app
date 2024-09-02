
from django.urls import path
from . import views
from .views import home, records, RecipeListView, RecipeDetailView, about
from django.conf import settings
from django.conf.urls.static import static

app_name = "recipes"

urlpatterns = [
   path('', views.home, name='home'),  # Homepage view
   path('list/', views.RecipeListView.as_view(), name='list'),  # URL pattern for showing all recipes
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
   path('recipes/records/', views.records, name='records'),
   path('recipes/about/', views.about, name='about'),
   path('add/', views.add_recipe, name='add_recipe'),
]