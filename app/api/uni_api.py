import aiohttp

async def format_unis(country_name: str, session: aiohttp.ClientSession):
    """
    Format Universities names from fetcher function into string

    :param session: session to send async requests
    :type session: aiohttp.ClientSession
    """
    fetched_uni = await fetch_unis(country_name, session) # get unis data from fetcher function
    if fetched_uni is not None:
        # format into list and send formatted message if the data has been retrieved correctly
        uni_list = format_uni_list(fetched_uni)
        return f""" 🎓 UNIVERSITIES
    {uni_list}

"""
    else:
        # send "Oops" message if the data hasn't been corretly gathered
        return """ 🎓 UNIVERSITIES
    Oops... Service Unavailable!

"""
    
async def fetch_unis(country_name: str, session: aiohttp.ClientSession):
    """
    Fetch three universities from given country using HipoLabs API 

    :param session: session to send async requests
    :type session: aiohttp.ClientSession
    """
    try:
        # send async request to HipoLabs API
        async with session.get(f"http://universities.hipolabs.com/search?country={country_name}") as response:
            response.raise_for_status()     # raise an Exception for 4xx and 5xx responses
            data = await response.json()    # convert data into list
            # prepare variables
            uni_list = []
            i = 0
            # get single uni data
            for uni in data:
                i += 1
                uni_list.append(uni['name'])
                if i == 3:
                    # quit when three universities are retrieved
                    break
            return uni_list
    except Exception:
        return None                         # return None if there are problems while fetching

def format_uni_list(uni_list: list):
    """
    Format Universities list into correct string
    """
    return ' - '.join(uni_list)
