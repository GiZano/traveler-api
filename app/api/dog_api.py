import aiohttp

async def format_dog(session: aiohttp.ClientSession):
    """
    Format data given by random dog fetcher

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    dog = await fetch_dog(session)  # get data from fetcher function
    if dog is not None:
        # send message with dog image url if it has been fetched correctly
        return f""" 🐶 RANDOM DOG
    URL: {dog}

"""
    else:
        # send "Oops" message if the image hasn't been fetched correctly
        return """ 🐶 RANDOM DOG
    Oops... Service Unavailable!

"""
    
async def fetch_dog(session: aiohttp.ClientSession):
    """
    Fetch random dog picture from Dog API

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    try:
        # send async request to Dog API
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            response.raise_for_status()     # raise and Exception with 4xx and 5xx responses
            data = await response.json()    # convert data into dict
            return data['message']          # return "message", which contains the url of the image
    except Exception:
        return None                         # return None if there are problems while fetching