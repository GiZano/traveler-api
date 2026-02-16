import requests

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

    message = f""" 🌤️ WEATHER IN {capital_name.upper()} 
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