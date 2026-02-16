import aiohttp

async def format_cat_fact(session: aiohttp.ClientSession):
    """
    Format random cat fact from fetcher into string

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    fact = await fetch_cat_fact(session)  # get fact from getcher function
    if fact is not None:
        # return message with fact if it has been retrieved correctly
        return f""" 🐱 CAT FACT
    {fact}

"""
    else:
        # return "Oops" message if the fact hasn't been fetched
        return """ 🐱 CAT FACT
    Oops... Service Unavailable

"""

async def fetch_cat_fact(session: aiohttp.ClientSession):
    """
    Fetch random cat fact from Cat Facts API

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    try:
        # send async request to Cat Facts API
        async with session.get("https://catfact.ninja/fact") as response:   
            response.raise_for_status()  # raise an Exception for responses with 4xx or 5xx
            data = await response.json() # convert data into dict
            return data['fact']          # return fact
    except Exception:
        return None                      # return None if there has been problems while fetching