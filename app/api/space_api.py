import aiohttp

async def format_photo(session: aiohttp.ClientSession):
    """
    Format data from Nasa API using helper functions

    :param session: session to send async requests
    :type session: aiohttp.ClientSession
    """
    photo_data = await fetch_photo(session) # save retrieved data from fetcher function
    # format data using helper functions
    if photo_data is not None:
        return f""" 📸 SPACE PHOTO
    Title: {get_title(photo_data)}
    URL: {get_url(photo_data)}

"""
    else:
        return """ 📸 SPACE PHOTO
    Oops... Service Unavailable!

"""
    
async def fetch_photo(session: aiohttp.ClientSession):
    """
    Fetch today's photo using NASA API

    :param session: session to send async requests
    :type session: aiohttp.ClientSession
    """
    try:
        # send async request to NASA API
        async with session.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY") as response:
            response.raise_for_status()     # raise an Exception for 4xx and 5xx responses
            return await response.json()    # return response turned in a dict
    except Exception:
        return None                         # return None if there are problems while fetching

def get_title(photo_data: dict):
    """
    Return photo title from given dict
    
    :param photo_data: dict containing photo data
    :type photo_data: dict
    """
    return photo_data['title']

def get_url(photo_data: dict):
    """
    Return photo url from given dict
    
    :param photo_data: dict containing photo data
    :type photo_data: dict
    """
    return photo_data['url']

