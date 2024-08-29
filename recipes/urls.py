
from django.urls import path
from . import views
from .views import home
from .views import RecipeListView, RecipeDetailView


app_name = "recipes"

urlpatterns = [
   path('', views.home, name='home'),  # Homepage view
   path('list/', views.RecipeListView.as_view(), name='list'),  # URL pattern for showing all recipes
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]