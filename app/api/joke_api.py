import aiohttp

async def format_joke(session: aiohttp.ClientSession):
    """
    Format random joke fetched by helper function into string

    :param session: session to send async requests
    :type session: aiohttp.ClientSession
    """
    joke = await fetch_joke(session) # get the joke using the fetched function
    if joke is not None:
        # return message with joke if it has been correctly fetched
        return f""" 😂 TRAVEL JOKE
    {joke}

"""
    else:
        # return "Oops" message if the joke hasn't been correctly fetched
        return f""" 😂 TRAVEL JOKE
    Oops... Service Unavailable!

"""

async def fetch_joke(session: aiohttp.ClientSession):
    """
    Fetch random joke from JokeAPI

    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    try:
        # send async request to JokeAPI
        async with session.get("https://v2.jokeapi.dev/joke/Any?lang=en&type=single") as response:
            response.raise_for_status()     # raise an Exception for 4xx or 5xx responses
            data = await response.json()    # convert response into dict
            return data['joke']             # return joke
    except Exception:
        return None                         # return None if there are problems while fetching