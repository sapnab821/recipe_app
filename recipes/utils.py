from recipes.models import Recipe   #you need to connect parameters from recipes model
from io import BytesIO  
import base64
import matplotlib.pyplot as plt
import pandas as pd

def get_graph():
   #create a BytesIO buffer for the image
    buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
    buffer.seek(0)

   #retrieve the content of the file
    image_png=buffer.getvalue()

   #encode the bytes-like object
    graph=base64.b64encode(image_png)

   #decode to get the string as output
    graph=graph.decode('utf-8')

   #free up the memory of buffer
    buffer.close()

    #return the image/graph
    with open('test_image.png', 'wb') as f:
        f.write(image_png)
    
    return base64.b64encode(image_png).decode('utf-8')
#define a function that takes the ID

def get_recipe_name_from_id(value):
    """
    Retrieve the name of a recipe given its ID.

    :param value: The ID of the recipe.
    :return: The name of the recipe or an error message if the recipe is not found.
    """
    try:
        recipe_name = Recipe.objects.get(id=value).name
    except Recipe.DoesNotExist:
        recipe_name = f"Recipe {value} (Not Found)"
    except Exception as e:
        # Handle unexpected errors during the operation
        recipe_name = f"Error fetching recipe name"
    return recipe_name

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':
        
        plt.bar(data['cooking_time'], data['ingredient_count'], color=['#66B2FF'])
        
        plt.xlabel('Cooking time')
        plt.ylabel('Number of Ingredients')
        

    elif chart_type == '#2':
        # Define the buckets
        bins = [0, 10, 30, float('inf')]
        labels = ['0-10 min', '11-30 min', 'Over 30 min']
        
        # Create a new column for cooking time buckets
        data['time_bucket'] = pd.cut(data['cooking_time'], bins=bins, labels=labels, right=False)
        
        # Count the number of recipes in each bucket
        time_bucket_counts = data['time_bucket'].value_counts()
        labels = time_bucket_counts.index
        values = time_bucket_counts.values
        
        plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['#FF9999', '#66B2FF', '#99FF99'])
        plt.title('Recipes by Cooking Time')
    elif chart_type == '#3':
        plt.plot(data['name'], data['cooking_time'], color='#FF9999')
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time')
        plt.xticks(rotation=30, ha='right')
    else:
        print('Unknown chart type')

    plt.tight_layout()

    chart = get_graph()
    
    return chart


def get_recipename_from_id(val):
    try:
        recipename = Recipe.objects.get(id=val)
        return recipename.name
    except Recipe.DoesNotExist:
        return 'Unknown Recipe'
