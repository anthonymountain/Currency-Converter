def json_parser(parse):
    """
    Parse the API response into a simplified dictionary format.

    Args:
        parse (dict): JSON response from API.

    Returns:
        dict: Dictionary with currency codes as keys and their values as the
        exchange rates.
    """
    try:
        data = parse.get("data", {})
        parsed = {currency: details["value"] for currency, details in data.items()}
        return parsed
    except KeyError as e:
        raise ValueError(f"Unexpected response format: {e}")
