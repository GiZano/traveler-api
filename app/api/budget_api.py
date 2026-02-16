import requests

def formatTravelCost(budget: int, startCurrency: str, endCurrency: str):
    """
    Fetches the converted rate from budgetConverter and formats it for output
    
    :param budget: given by the user
    :type budget: int
    :param startCurrency: currency from which convert
    :type startCurrency: str
    :param endCurrency: currency into which convert
    :type endCurrency: str
    """
    # create pre-formatted message and insert correct data
    message = f""" 💰 BUDGET
    {budget} {startCurrency} = {'{0:.2f}'.format(budgetConverter(budget, startCurrency, endCurrency))} {endCurrency}

"""

    return message

def budgetConverter(budget: int, startCurrency: str, endCurrency: str):
    """
    Using fetchConverRate output, convert the given budget from given startCurrency into given endCurrency
    
    :param budget: given by the user
    :type budget: int
    :param startCurrency: currency from which convert
    :type startCurrency: str
    :param endCurrency: currency into which convert
    :type endCurrency: str
    """
    # return given budget times the rate from the fetcher
    return budget * float(fetchConvertRate(startCurrency, endCurrency))

def fetchConvertRate(startCurrency: str, endCurrency: str):
    """
    Using ExchangeRateAPI, fetches the convertion rate from startCurrency to endCurrency
    
    :param startCurrency: currency from which convert
    :type startCurrency: str
    :param endCurrency: currency into which convert
    :type endCurrency: str
    """
    # get convertion rates of the given startCurrency
    response = requests.get(f"https://open.er-api.com/v6/latest/{startCurrency}")
    # transform the json into usable list/dict
    data = response.json()
    # get the rate for the selected endCurrency
    return data['rates'][endCurrency]




