from api_client import retrieve_conversion


def convert(amount, base, targets):
    """
    Convert the given amount from a base currency to target currencies.

    Args:
        amount (float): The amount to convert.
        base (str): The base currency code.
        targets (list of str): List of target currency codes.

    Returns:
        dict: Dictionary where keys are target currencies and values are
        converted amounts.
    """
    rates = retrieve_conversion(base, targets)
    amounts = {}
    for rate in rates:
        amounts[rate] = amount * rates[rate]
    return amounts
