import requests

def infoPrinter(country: str):
    """
    Build swindle sheet for final user
    
    :param country: country name
    :type country: str
    """

    info_header = """
╔══════════════════════════════════════════╗
║        SWINDLE SHEET - CURIOUSTRIP       ║
╠══════════════════════════════════════════╣
"""
    info_footer = "╚══════════════════════════════════════════╝"

    try:
        print(info_header)

        ### PHASE 0. COUNTRY DATA FETCH ###

        country_data = fetchDestination(country)

        if isinstance(country_data, dict):
            raise Exception(f"Country {country} doesn't exist!")
        
        ### PHASE 1. DESTINATION DATA FORMAT ###

        print(formatDestination(country_data))

        ### PHASE 2. WEATHER DATA FETCH AND FORMAT ###

        weather_data = fetchWeather(country_data[0]['latlng'])
        
        print(formatWeather(country_data[0]['capital'][0], weather_data))
        

    except Exception as e :
        info_footer = f"Country Data Service Isn't Responding! - {e} \n" + info_footer

    print(info_footer)

def fetchDestination(country: str):
    """
    Fetch destination data based on restcountries API and given country name
    
    :param country: country name
    :type country: str
    """


    data = ''


    response = requests.get("https://restcountries.com/v3.1/name/" + country)

    data = response.json()

    return data

def formatDestination(country_data: list):
    """
    Formats the given data of the selected country
    
    :param country_data: Data of the chosen country
    :type country_data: list
    """


    country = country_data[0]
    official_name = country['name']['official']
    capital_city  = country['capital'][0]
    population    = country['population']
    continents = ''

    for continent in country['continents']:
        continents = continents + "\n" + "       - " + continent + ","
    
    languages = ''

    for language in country['languages']:
        languages = languages + "\n" + "       - " + country['languages'][language].title() + ","

    languages = languages[:-1]

    currencies = ''

    for currency in country['currencies']:
        currencies = currencies + "\n" + "     - " + country['currencies'][currency]['name'].title()

    message = f"""
📍 DESTINATION
    Country: {official_name}
    Capital: {capital_city}
    Population: {population:,}
    Continent: {continent}
    Language/s: {languages}
    Currency: {currencies}
    """

    return message

def fetchWeather(latlng: list):
    """
    Fetch weather data about the selected country from OPEN METEO API
    
    :param latlng: Latitude and Longitude data
    :type latlng: list
    """

    lat = latlng[0]
    lon = latlng[1]
        
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    data = response.json()

    return data

def formatWeather(capital_name:str, weather_data: dict):
    """
    Formats the given weather data of the selected country
    
    :param capital_name: Name of the country capital
    :type country_name: str
    :param weather_data: Data of the chosen country
    :type weather_data: dict
    """

    temperature = str(weather_data['current_weather']['temperature']) + str(weather_data['current_weather_units']['temperature'])
    wind        = str(weather_data['current_weather']['windspeed']) + str(weather_data['current_weather_units']['windspeed'])
    weather_code = weather_data['current_weather']['weathercode']

    message = f"""
🌤️ WEATHER IN {capital_name.upper()} 
    Temperature: {temperature}
    Wind: {wind}
    Weather: {decodeWeather(weather_code)}
    """


    return message

def decodeWeather(weather_code: int):
    """
    Decodes the weathercode given by the weather API into his textual meaning
    
    :param weather_code: weather code given by the api
    :type weather_code: int
    """

    match weather_code:
        case 0:
            return '☀️​ Clear Sky'
        case 1:
            return '⛅​ Mainly Clear'
        case 2:
            return '⛅​ Partly Cloudy'
        case 3:
            return '⛅​ Overcast'
        case 45:
            return '🌁​ Foggy'
        case 48:
            return '🌁​ Rime Fog'
        case 51:
            return '🌦️ Light Drizzle'
        case 53:
            return '🌦️ Moderate Drizzle'
        case 55:
            return '🌦️ Dense Drizzle'
        case 56:
            return '🌦️​🧊​ Light Freezing Drizzle'
        case 57:
            return '🌦️​🧊​ Dense Freezing Drizzle'
        case 61:
            return '🌧️ Slight Rain'
        case 63:
            return '🌧️ Moderate Rain'
        case 65:
            return '🌧️ Heavy Rain'
        case 66:
            return '🌧️​🧊​ Light Freezing Rain'
        case 67:
            return '🌧️🧊 Heavy Freezing Rain'
        case 71:
            return '🌨️ Slight Snow Fall'
        case 73:
            return '🌨️ Moderate Snow Fall'
        case 75:
            return '🌨️ Heavy Snow Fall'
        case 77:
            return '🌨️🧊 Snow Grains'
        case 80:
            return '🌧️🌧️ Slight Rain Shower'
        case 81:
            return '🌧️🌧️ Moderate Rain Shower'
        case 82:
            return '🌧️🌧️ Violent Rain Shower'  
        case 85:
            return '🌨️🌨️ Slight Snow Shower'
        case 86:
            return '🌨️🌨️ Heavy Snow Shower'
        case 95:
            return '⛈️ Slight Thunderstorm'
        case 96:
            return '⛈️🧊 Thunderstorm with Slight Hail'
        case 99:
            return '⛈️🧊 Thunderstorm with Heavy Hail'
        case default:
            return "Extreme Conditions!!"