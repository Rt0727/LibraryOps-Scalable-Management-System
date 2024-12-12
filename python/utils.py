import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def validate_input(input_value, value_type):
    try:
        return value_type(input_value)
    except ValueError:
        logging.error("Invalid input type. Expected %s", value_type)
        return None