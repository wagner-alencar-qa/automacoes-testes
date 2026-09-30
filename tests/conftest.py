from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

from guara.application import Application
from tests.config.driver_config import get_driver


@pytest.fixture
def driver():
    """Fixture to provide a WebDriver instance for tests."""
    driver = get_driver(browser="firefox")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def app(driver):
    """Fixture to provide an Application instance with Guará support."""
    return Application(driver)
