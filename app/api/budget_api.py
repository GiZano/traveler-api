import aiohttp

async def format_travel_cost(budget: int, start_currency: str, end_currency: str, session: aiohttp.ClientSession):
    """
    Fetches the converted rate from budget_converter and formats it for output
    
    :param budget: given by the user
    :type budget: int
    :param start_currency: currency from which convert
    :type start_currency: str
    :param end_currency: currency into which convert
    :type end_currency: str
    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    # get converted budget from converter
    converted_budget = await budget_converter(budget, start_currency, end_currency, session)
    if converted_budget is not None:
        # return if converted budget as been correctly generated
        return f""" 💰 BUDGET
        {budget} {start_currency} = {'{0:.2f}'.format(converted_budget)} {end_currency}

"""
    else:
        # return "Oops message if the budget hasn't been generated correctly"
        return f""" 💰 BUDGET
        Oops... Service Unavailable!

"""

async def budget_converter(budget: int, start_currency: str, end_currency: str, session: aiohttp.ClientSession):
    """
    Using fetchConverRate output, convert the given budget from given start_currency into given end_currency
    
    :param budget: given by the user
    :type budget: int
    :param start_currency: currency from which convert
    :type start_currency: str
    :param end_currency: currency into which convert
    :type end_currency: str
    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    # fetch convert rate using helper function
    rate = await fetch_convert_rate(start_currency, end_currency, session)
    if rate:
        # if rate has been correctly generated, return the converted budget
        return budget * rate
    else:
        # if the rate hasn't been fetched, return None
        return None

async def fetch_convert_rate(start_currency: str, end_currency: str, session: aiohttp.ClientSession):
    """
    Using ExchangeRateAPI, fetches the convertion rate from start_currency to end_currency
    
    :param start_currency: currency from which convert
    :type start_currency: str
    :param end_currency: currency into which convert
    :type end_currency: str
    :param session: session to send async requests
    :type session: aiohttp.ClientSession 
    """
    try:
        # send async requests to fetch convert rates
        async with session.get(f"https://open.er-api.com/v6/latest/{start_currency}") as response:
            response.raise_for_status()         # raise exception if code is 4xx or 5xx
            data = await response.json()        # convert data into dict
            return data['rates'][end_currency]  # return rate of given end_currency
    except Exception:
        return None                             # if there are problems while fetching, return