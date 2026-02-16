import aiohttp

async def fetchWeather(latlng: list, session: aiohttp.ClientSession):
    """
    Fetch weather data about the selected country from Open Meteo API
    
    :param latlng: Latitude and Longitude data
    :type latlng: list
    :param session: session for async requests
    :type session: aiohttp.ClientSession
    """
    # separate latitude and longitude from given list
    lat = latlng[0]
    lon = latlng[1]
    try:
        # send async request to Open Meteo API
        async with session.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true") as response:
            response.raise_for_status()     # raise an Exception for 4xx and 5xx responses
            data = await response.json()    # convert data into dict
            return data
    except aiohttp.ClientError:
        return None                         # return None if there are problems while fetching

async def formatWeather(capital_name:str, latlng: list, session: aiohttp.ClientSession):
    """
    Formats the given weather data of the selected country
    
    :param capital_name: capital name of the given country
    :type capital_name: str
    :param latlng: latitude and longitude of the given capital
    :type latlng: list
    :param session: client session for async requests
    :type session: aiohttp.ClientSession
    """
    weather_data = await fetchWeather(latlng, session)  # get data from fetcher function

    if weather_data is not None:
        # if data has been correctly gathered, format it using helper functions
        return f""" 🌤️ WEATHER IN {capital_name.upper()} 
    Temperature: {get_temperature(weather_data)}
    Wind: {get_wind(weather_data)}
    Weather: {decodeWeather(get_weather_code(weather_data))}

"""
    else:
        # send "Oops" message if data hasn't been correctly gathered
        return f""" 🌤️ WEATHER IN {capital_name.upper()} 
    Oops... Service Unavailable!

"""

def get_temperature(weather_data: dict):
    """
    Return temperature of given weather data from Open Meteo API
    
    :param weather_data: weather data from API
    :type weather_data: dict
    """
    return str(weather_data['current_weather']['temperature']) + str(weather_data['current_weather_units']['temperature'])

def get_wind(weather_data: dict):
    """
    Return wind of given weather data from Open Meteo API
    
    :param weather_data: Description
    :type weather_data: dict
    """
    return str(weather_data['current_weather']['windspeed']) + str(weather_data['current_weather_units']['windspeed'])

def get_weather_code(weather_data: dict):
    """
    Return weather code of given weather data from Open Meteo API
    
    :param weather_data: Description
    :type weather_data: dict
    """
    return weather_data['current_weather']['weathercode']

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