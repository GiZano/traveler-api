import requests

def formatRandomRecipe():
    """
    Use fetchRandomRecipe to generate a random recipe and format given data into a string
    """
    # use fetcher function to retrieve a random recipe data
    recipe_data = fetchRandomRecipe()
    # format data using helper functions
    message = f""" 🍽️ CHEF'S SUGGESTION:
    Plate: {getName(recipe_data)}
    Category: {getCategory(recipe_data)}
    Ingredients: {formatIngredients(getIngredients(recipe_data))}

"""
    return message

def fetchRandomRecipe():
    """
    Fetch a random recipe from TheMealDB
    """
    # fetch data from TheMealDB
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    # return usable list/dict
    return response.json()

def getName(recipe_data: dict):
    """
    Retrieve plate name from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    return recipe_data['meals'][0]['strMeal']

def getCategory(recipe_data: dict):
    """
    Retrieve plate category from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    return recipe_data['meals'][0]['strCategory']

def getIngredients(recipe_data: dict):
    """
    Retrieve plate ingredients from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    ingredients = []

    for i in range(1, 6):
        ingredient = recipe_data['meals'][0][f'strIngredient{i}']
        if ingredient != '':
            ingredients.append(ingredient)

    return ingredients

def formatIngredients(ingredients: list):
    """
    Format ingredients list from getIngredients function into a string
    
    :param ingredients: given ingredients list
    :type ingredients: list
    """
    # format single ingredients into string like: "ing1, ing2 ... ingN"
    return ', '.join(ingredients)