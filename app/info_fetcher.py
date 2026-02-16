### Import libs for async calls ###
import asyncio, aiohttp
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

async def fetchInfo(country_name: str, given_budget: int, session: aiohttp.ClientSession):
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

    info = [None, None]

    try:
        ### PHASE 0. COUNTRY DATA FETCH ###
            
        country_data = await country.fetch_destination(country_name, session)

        if isinstance(country_data, dict):
            errors.append(f'Country {country_name} doesn\' exist!')
            raise Exception(f"Country {country_name} doesn't exist!")
        
        ### PHASE 1. DESTINATION DATA FORMAT ###

        data.append(country.format_destination(country_data))

        data.extend(
            await asyncio.gather(
                ### PHASE 2. WEATHER DATA FETCH AND FORMAT ###
                weather.formatWeather(country.get_capital_city(country_data), country.get_position(country_data), session),
                ### PHASE 3. CONVERT GIVEN BUDGET INTO LOCAL CURRENCY
                budget.format_travel_cost(given_budget, 'EUR', country.get_currency(country_data)[0], session),
                ## 6.3 UNIVERSITIES ##
                uni.format_unis(country.get_common_name(country_data), session),
                ### PHASE 4. GET A RANDOM RECIPE ###
                food.format_random_recipe(session),
                ### PHASE 5. TODAY'S CURIOSITIES ###
                ## 5.1 CAT FACTS ##
                cat.format_cat_fact(session),
                ## 5.2 RANDOM JOKE ##
                joke.format_joke(session),
                ### PHASE 6. BONUS DATA ###
                ## 6.1 SPACE PHOTO
                space.format_photo(session),
                ## 6.2 RANDOM DOG ##
                dog.format_dog(session)
            )
        )

        #### INFO FETCHING END ####
        info[0] = info_header + ''.join(data) + info_footer
        info[1] = country.get_common_name(country_data)

    except Exception:
        errors.append('Country Data Service Isn\'t Responding!')

    return info