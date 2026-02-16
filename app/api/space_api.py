import requests

def formatPhoto():
    """
    Format data from Nasa API using helper functions
    """
    # save retrieved data from fetcher function
    photo_data = fetchPhoto()
    # format data using helper functions
    message = f""" 📸 SPACE PHOTO
    Title: {getTitle(photo_data)}
    URL: {getURL(photo_data)}

"""
    return message
    
def fetchPhoto():
    """
    Fetch today's photo using NASA API
    """
    # fetch data from NASA API
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    # convert response into dict and return it
    return response.json()

def getTitle(photo_data: dict):
    """
    Return photo title from given dict
    
    :param photo_data: dict containing photo data
    :type photo_data: dict
    """
    return photo_data['title']

def getURL(photo_data: dict):
    """
    Return photo url from given dict
    
    :param photo_data: dict containing photo data
    :type photo_data: dict
    """
    return photo_data['url']

