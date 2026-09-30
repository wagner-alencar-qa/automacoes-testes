"""
WebDriver configuration and initialization.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from tests.config.settings import HEADLESS_MODE, WINDOW_SIZE


def create_firefox_driver():
    """Create and configure Firefox WebDriver."""
    options = FirefoxOptions()
    if HEADLESS_MODE:
        options.add_argument("-headless")
    options.add_argument(f"--width={WINDOW_SIZE[0]}")
    options.add_argument(f"--height={WINDOW_SIZE[1]}")
    driver = webdriver.Firefox(options=options)
    return driver


def create_chrome_driver():
    """Create and configure Chrome WebDriver."""
    options = ChromeOptions()
    if HEADLESS_MODE:
        options.add_argument("--headless")
    options.add_argument(f"--window-size={WINDOW_SIZE[0]},{WINDOW_SIZE[1]}")
    driver = webdriver.Chrome(options=options)
    return driver


def get_driver(browser="firefox"):
    """Get WebDriver instance based on specified browser."""
    if browser.lower() == "chrome":
        return create_chrome_driver()
    return create_firefox_driver()
