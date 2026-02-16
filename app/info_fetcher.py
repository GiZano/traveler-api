### Import all needed APIs to fetch all needed data ###
import api.country_api as country
import api.weather_api as weather
import api.budget_api  as budget
import api.food_api    as food
import api.cat_api     as cat
import api.joke_api    as joke
import api.space_api   as space
import api.dog_api     as dog
import api.uni_api     as uni

def fetchInfo(country_name: str, given_budget: int):
    """
    Build swindle sheet for final user
    
    :param country_name: given by user
    :type country: str
    :param given_budget: given by user
    :type given_budget: int
    """

    info_header = """
╔══════════════════════════════════════════╗
║        SWINDLE SHEET - CURIOUSTRIP       ║
╠══════════════════════════════════════════╣
"""
    info_footer = "╚══════════════════════════════════════════╝"

    errors = []

    data = []

    try:
        ### PHASE 0. COUNTRY DATA FETCH ###
            
        country_data = country.fetchDestination(country_name)

        if isinstance(country_data, dict):
            errors.append(f'Country {country_name} doesn\' exist!')
            raise Exception(f"Country {country_name} doesn't exist!")
        
        ### PHASE 1. DESTINATION DATA FORMAT ###

        data.append(country.formatDestination(country_data))

        ### PHASE 2. WEATHER DATA FETCH AND FORMAT ###

        try:
            data.append(weather.formatWeather(country.getCapitalCity(country_data), weather.fetchWeather(country.getPosition(country_data))))
        except:
            errors.append('Weather Data Unavailable!')

        ### PHASE 3. CONVERT GIVEN BUDGET INTO LOCAL CURRENCY

        try:
            data.append(budget.formatTravelCost(given_budget, 'EUR', country.getCurrency(country_data)[0]))
        except:
            errors.append('Currency Convert Rate Data Unavailable!')

        ## 6.3 UNIVERSITIES ##

        try:
            data.append(uni.formatUnis(country.getCommonName(country_data)))
        except:
            errors.append('University List Service Unavailable!')

        ### PHASE 4. GET A RANDOM RECIPE ###

        try:
            data.append(food.formatRandomRecipe())
        except:
            errors.append('Random Recipe Generator Unavailable!')

        ### PHASE 5. TODAY'S CURIOSITIES ###

        ## 5.1 CAT FACTS ##

        try:
            data.append(cat.formatCatFact())
        except:
            errors.append('Cat Facts Generator Unavailable!')

        ## 5.2 RANDOM JOKE ##

        try:
            data.append(joke.formatJoke())
        except:
            errors.append('Joke Generator Unavailable!')

        ### PHASE 6. BONUS DATA ###

        ## 6.1 SPACE PHOTO

        try:
            data.append(space.formatPhoto())
        except:
            errors.append('Space Photo Service Unavailable!')

        ## 6.2 RANDOM DOG ##

        try:
            data.append(dog.formatDog())
        except:
            errors.append('Random Dog Service Unavailable!')

        #### INFO FETCHING END ####

    except Exception:
        errors.append('Country Data Service Isn\'t Responding!')
    
    if len(errors) > 0:
        info_footer = 'Errors: \n   - ' + '\n   - '.join(errors) + '\n\n' + info_footer

    info = []
    info.append(info_header + ''.join(data) + info_footer)
    info.append(country.getCommonName(country_data))

    return info