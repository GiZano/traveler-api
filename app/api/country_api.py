import aiohttp

async def fetch_destination(country: str, session: aiohttp.ClientSession):
    """
    Fetch destination data based on restcountries API and given country name
    
    :param country: country name
    :type country: str
    :param session: session for async requests
    :type session: aiohttp.ClientSession
    """
    try:
        # fetch country data from REST Countries API
        async with session.get("https://restcountries.com/v3.1/name/" + country) as response:
            response.raise_for_status       # raise an Exception for 4xx or 5xx responses
            data = await response.json()    # convert data into list
            return data                     # return list
    except Exception:
        return None                         # return None if there are problems while fetching

def format_destination(country_data: list):
    """
    Formats the given data of the selected country
    
    :param country_data: data given by the API
    :type country_data: list
    """
    # format given data using helper functions
    message = f""" 
 📍 DESTINATION
    Country: {get_off_name(country_data)}
    Capital: {get_capital_city(country_data)}
    Population: {get_population(country_data):,}
    Continent: {get_continent(country_data)}
    Language/s: {get_language(country_data)}
    Currency: {get_currency(country_data)[1]}

"""
    return message

def get_off_name(country_data: list):
    """
    Get official name of a country using data given by REST Countries API
    
    :param country_data:data given by the API
    :type country_data: list
    """
    return country_data[0]['name']['official']

def get_common_name(country_data: list):
    """
    Get common name of a country using data given by REST Countries API
    
    :param country_data:data given by the API
    :type country_data: list
    """
    return country_data[0]['name']['common']

def get_capital_city(country_data: list):
    """
    Get capital city of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    return country_data[0]['capital'][0]

def get_population(country_data: list):
    """
    Get population of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    return country_data[0]['population']

def get_continent(country_data: list):
    """
    Get continent of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    continents = ''

    for continent in country_data[0]['continents']:
        continents = continents + "\n" + "       - " + continent + ","

    return continents

def get_language(country_data: list):
    """
    Get languages of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    languages = ''

    for language in country_data[0]['languages']:
        languages = languages + "\n" + "       - " + country_data[0]['languages'][language].title() + ","
    return languages

def get_currency(country_data: list):
    """
    Get currency ( [abbr, fullName ]) of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    currencies = []

    for currency in country_data[0]['currencies']:
        currencies.append(str(currency))
        currencies.append(country_data[0]['currencies'][currency]['name'].title())
        
    return currencies

def get_position(country_data: list):
    """
    Get position of a country ( [latitude, logitude] ) using data given by REST Countries API
    
    :param country_data: Description
    :type country_data: list
    """
    return country_data[0]['latlng']