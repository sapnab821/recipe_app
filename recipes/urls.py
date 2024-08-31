
from django.urls import path
from . import views
from .views import home, records
from .views import RecipeListView, RecipeDetailView, RecipeSearchForm
from django.conf import settings
from django.conf.urls.static import static

app_name = "recipes"

urlpatterns = [
   path('', views.home, name='home'),  # Homepage view
   path('list/', views.RecipeListView.as_view(), name='list'),  # URL pattern for showing all recipes
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
   path('recipes/records/', records, name='records'),
   path('recipes/records/', views.records, name='records'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)