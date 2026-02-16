import requests

def formatCatFact():
    """
    Format random cat fact from fetcher into string
    """

    message = f""" 🐱 CAT FACT
    {fetchCatFact()}

"""
    return message

def fetchCatFact():
    """
    Fetch random cat fact from Cat Facts API
    """
    # fetch data from Cat Facts API
    response = requests.get("https://catfact.ninja/fact")
    # convert retrieved json into usable dict/list
    data = response.json()
    # return fact from data (dict)
    return data['fact']