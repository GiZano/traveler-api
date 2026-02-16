import requests

def formatUnis(country_name: str):
    """
    Format Universities names from fetcher function into string
    """
    message = f""" 🎓 UNIVERSITIES
    {formatUniList(fetchUnis(country_name))}

"""
    return message
    
def fetchUnis(country_name: str):
    """
    Fetch three universities from given country using HipoLabs API 
    """
    # fetch data from HipoLabs API
    response = requests.get(f"http://universities.hipolabs.com/search?country={country_name}")
    # convert data into usable list
    data = response.json()
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

def formatUniList(uni_list: list):
    """
    Format Universities list into correct string
    """
    return ' - '.join(uni_list)
