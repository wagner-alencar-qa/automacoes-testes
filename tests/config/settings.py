"""
Configuration settings for test automation.
"""

BASE_URL = "https://www.saucedemo.com"
HEADLESS_MODE = True
WINDOW_SIZE = (1920, 1080)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10

# Test user credentials
TEST_USERS = {
    "standard_user": {
        "username": "standard_user",
        "password": "secret_sauce",
    },
    "invalid_user": {
        "username": "invalid_user",
        "password": "invalid_password",
    },
    "locked_user": {
        "username": "locked_out_user",
        "password": "secret_sauce",
    },
}

# Test data
TEST_PRODUCTS = {
    "backpack": "sauce-labs-backpack",
    "bike_light": "sauce-labs-bike-light",
    "bolt_tshirt": "sauce-labs-bolt-t-shirt",
}

CHECKOUT_DATA = {
    "first_name": "Ana",
    "last_name": "Silva",
    "zip_code": "01000-000",
}
