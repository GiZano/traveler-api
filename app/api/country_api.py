import requests

def fetchDestination(country: str):
    """
    Fetch destination data based on restcountries API and given country name
    
    :param country: country name
    :type country: str
    """
    # fetch data from API
    response = requests.get("https://restcountries.com/v3.1/name/" + country)
    # convert given json into a list or dict based on API output
    data = response.json()

    return data

def formatDestination(country_data: list):
    """
    Formats the given data of the selected country
    
    :param country_data: data given by the API
    :type country_data: list
    """

    message = f""" 
 📍 DESTINATION
    Country: {getOffName(country_data)}
    Capital: {getCapitalCity(country_data)}
    Population: {getPopulation(country_data):,}
    Continent: {getContinent(country_data)}
    Language/s: {getLanguage(country_data)}
    Currency: {getCurrency(country_data)[1]}

"""
    return message

def getOffName(country_data: list):
    """
    Get official name of a country using data given by REST Countries API
    
    :param country_data:data given by the API
    :type country_data: list
    """
    return country_data[0]['name']['official']

def getCommonName(country_data: list):
    """
    Get common name of a country using data given by REST Countries API
    
    :param country_data:data given by the API
    :type country_data: list
    """
    return country_data[0]['name']['common']

def getCapitalCity(country_data: list):
    """
    Get capital city of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    return country_data[0]['capital'][0]

def getPopulation(country_data: list):
    """
    Get population of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    return country_data[0]['population']

def getContinent(country_data: list):
    """
    Get continent of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    continents = ''

    for continent in country_data[0]['continents']:
        continents = continents + "\n" + "       - " + continent + ","

    return continents

def getLanguage(country_data: list):
    """
    Get languages of a country using data given by REST Countries API
    
    :param country_data: data given by the API
    :type country_data: list
    """
    languages = ''

    for language in country_data[0]['languages']:
        languages = languages + "\n" + "       - " + country_data[0]['languages'][language].title() + ","
    return languages

def getCurrency(country_data: list):
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

def getPosition(country_data: list):
    """
    Get position of a country ( [latitude, logitude] ) using data given by REST Countries API
    
    :param country_data: Description
    :type country_data: list
    """
    return country_data[0]['latlng']