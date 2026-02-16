import requests

def formatDog():
    """
    Format data given by random dog fetcher
    """
    message = f""" 🐶 RANDOM DOG
    URL: {fetchDog()}

"""
    return message
    
def fetchDog():
    """
    Fetch random dog picture from Dog API
    """
    # fetch data from API
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    # convert response into dict
    data = response.json()
    # return the image URL
    return data['message']