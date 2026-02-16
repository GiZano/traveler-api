import aiohttp

async def format_random_recipe(session: aiohttp.ClientSession):
    """
    Use fetch_random_recipe to generate a random recipe and format given data into a string

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    recipe_data = await fetch_random_recipe(session) # use fetcher function to retrieve a random recipe data
    # format data using helper functions
    if recipe_data is not None:
        return f""" 🍽️ CHEF'S SUGGESTION:
    Plate: {get_name(recipe_data)}
    Category: {get_category(recipe_data)}
    Ingredients: {format_ingredients(get_ingredients(recipe_data))}

"""
    else:
        return f""" 🍽️ CHEF'S SUGGESTION:
    Ooops... Service Unavailable!

"""

async def fetch_random_recipe(session: aiohttp.ClientSession):
    """
    Fetch a random recipe from TheMealDB

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    try:
        # fetch data using async requests
        async with session.get("https://www.themealdb.com/api/json/v1/1/random.php") as response:
            response.raise_for_status()     # raise Exception for 4xx or 5xx requests
            return await response.json()    # return response converted in dict
    except Exception:
        return None                         # return None if there are problems while fetching

def get_name(recipe_data: dict):
    """
    Retrieve plate name from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    return recipe_data['meals'][0]['strMeal']

def get_category(recipe_data: dict):
    """
    Retrieve plate category from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    return recipe_data['meals'][0]['strCategory']

def get_ingredients(recipe_data: dict):
    """
    Retrieve plate ingredients from recipe data from TheMealDB
    
    :param recipe_data: given recipe data
    :type recipe_data: dict
    """
    ingredients = []
    # get only the first 5 ingredients [ingredient1, ingredient2 ... ingredient5]
    for i in range(1, 6):
        ingredient = recipe_data['meals'][0][f'strIngredient{i}']
        if ingredient != '':
            ingredients.append(ingredient)

    return ingredients

def format_ingredients(ingredients: list):
    """
    Format ingredients list from get_ingredients function into a string
    
    :param ingredients: given ingredients list
    :type ingredients: list
    """
    # format single ingredients into string like: "ing1, ing2 ... ingN"
    return ', '.join(ingredients)