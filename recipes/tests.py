from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from django.urls import reverse
from django.test import Client

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(
            name="Omelette",
            cooking_time=10,
            ingredients="Eggs, Butter, Salt, Pepper, Onion, Bell Pepper, Ham",
        )

    # Test for recipe name being initialized
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    # Test for recipe name exceeding 100 characters
    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    # Test for recipe cooking_time being an integer
    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), int)

    # Test for recipe ingredients exceeding 225 characters in ingredients field
    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 225)

    # Test for recipe difficulty ensuring calculate_difficulty works
    def test_calculate_difficulty(self):
        recipe = Recipe.objects.get(id=self.recipe.id)

        # Set the cooking time and ingredients for the recipe
        recipe.cooking_time = 5
        recipe.ingredients = 'Ingredient1,Ingredient2'
        recipe.save()

        # Assert that the difficulty is 'easy'
        self.assertEqual(recipe.difficulty(), 'easy')

        # Modify the recipe to have a higher cooking time and more ingredients
        recipe.cooking_time = 15
        recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3,Ingredient4'
        recipe.save()

        # Assert that the difficulty is 'hard'
        self.assertEqual(recipe.difficulty(), 'hard')


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='johnnytest', password='testpassword')


class UserAuthTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_list_redirect_without_auth(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertRedirects(response, f'/login/?next={reverse("recipes:list")}')
    
    def test_list_redirect_with_auth(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:list'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')