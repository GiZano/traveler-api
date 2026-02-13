import requests

base_url = "https://restcountries.com/v3.1/name/"

def fetchCountry(country: str):
    
    response = requests.get(base_url + country)

    data = response.json()

    message = f"""
    Data of {country}:

    {formatCountry(data)}.

    """

    return message

def formatCountry(country: str):
    country = country[0]
    official_name = country['name']['official']
    capital_city  = country['capital']
    population    = country['population']
    continent = ''

    for cont in country['continents']:
        continent = continent + " - " + cont
    
    languages = ''

    for language in country['languages']:
        languages = languages + "\n" + "       - " + language

    currencies = ''

    for currency in country['currencies']:
        currencies = currencies + "\n" + "     - " + currency[0]['name']

    message = f"""
    - Official Name: {official_name},
    - Capital City: {capital_city},
    - Population: {population},
    - Continent/s: {continent},
    - Language/s: {languages},
    - Currency/ies: {currencies}

    """

    return message

