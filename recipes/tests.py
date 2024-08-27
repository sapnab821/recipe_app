from django.test import TestCase
from .models import Recipe

# Create your tests here.
# Create your tests here.
class RecipeModelTest(TestCase):
    # set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            ingredients="Tea leaves, Sugar, Water",
            cooking_time=5,
        )

    # NAME
    def test_recipe_name(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and use it to query its data
        max_length = recipe._meta.get_field("name").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 50)

    # INGREDIENTS
    def test_ingredients_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field("ingredients").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 225)

    # COOKING TIME
    def test_cooking_time_value(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'cooking_time' field and use it to query its data
        cooking_time_value = recipe.cooking_time

        # compare the value to the expected result
        self.assertIsInstance(cooking_time_value, int)


    def test_difficulty_max_length(self):
        # Verifies the difficulty field's maximum length is correctly set.
        max_length = self.recipe._meta.get_field('difficulty').max_length
        self.assertEqual(max_length, 20)

    def test_string_representation(self):
        # Tests the string representation of a Recipe object to ensure it returns its name.
        self.assertEqual(str(self.recipe), self.recipe.name)
    
    def test_return_ingredients_as_list(self):
        # Confirms ingredients stored as a string are correctly converted to a list.
        ingredients_list = self.recipe.return_ingredients_as_list()
        self.assertEqual(len(ingredients_list), 3)
    
    def test_calculate_difficulty(self):
        # Tests the logic that calculates a recipe's difficulty based on cooking time and ingredient count.
        self.recipe.cooking_time = 5
        self.recipe.ingredients = 'Ingredient1,Ingredient2'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Easy')
    
        self.recipe.cooking_time = 15
        self.recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3,Ingredient4'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Hard')
        
    def test_save_method_override(self):
        # Checks if the save method correctly sets the difficulty level based on cooking time and ingredients.
        self.recipe.cooking_time = 20
        self.recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Intermediate')
    
    def test_default_image_path(self):
        # Verifies that the default path for a recipe's image is correctly set.
        self.assertEqual(self.recipe.pic, 'no_picture')