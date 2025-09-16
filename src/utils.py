def normalize_input(input_data):
    """
    Convert string inputs from form to float and ensure numeric format.
    Ignores non-numeric issues gracefully.
    """
    cleaned_data = {}
    for key, value in input_data.items():
        try:
            cleaned_data[key] = float(value)
        except (ValueError, TypeError):
            cleaned_data[key] = 0.0
    return cleaned_data
