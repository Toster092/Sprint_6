from selenium import webdriver
import pytest
from data import Constants


@pytest.fixture
def driver():
 driver = webdriver.Firefox()
 driver.get(Constants.URL)
 yield driver
 driver.quit()