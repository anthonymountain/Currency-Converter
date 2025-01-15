import currencyapicom
from parser import json_parser


def retrieve_conversion(base, targets):
    """
    Retrieve the latest conversion rates for a base currency to a list of target
    currencies using the CurrencyAPI.

    Args: base (str): The base currency for conversion (e.g. 'USD').
    targets (list of str): A list of target currencies to retrieve rates for
    (e.g., ['EUR', 'GBP']).

    Returns:
        dict: A dictionary containing conversion rates where keys are target
        currencies and values are the conversion rates relative to the base
        currency.

    Example:
        >>> retrieve_conversion('USD', ['EUR', 'GBP'])
        {'EUR': 0.85, 'GBP': 0.75}
    """
    client = currencyapicom.Client(
        'cur_live_o8oJYU3fVyhpiJr6577uvEW6C8oglV8yFc5pV3Nh')
    result = client.latest(base, targets)
    return json_parser(result)
