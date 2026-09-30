from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
