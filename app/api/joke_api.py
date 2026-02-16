import requests

def formatJoke():
    """
    Format random joke fetched by helper function into string 
    """
    message = f""" 😂 TRAVEL JOKE
    {fetchJoke()}

"""
    return message

def fetchJoke():
    """
    Fetch random joke from JokeAPI
    """
    # fetch data from JokeAPI
    response = requests.get("https://v2.jokeapi.dev/joke/Any?lang=en&type=single")
    # convert response into usable dict
    data = response.json()
    # return joke
    return data['joke']    
