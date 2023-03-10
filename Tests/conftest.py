
import json
import pytest
import time
from configparser import ConfigParser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup(request):
    global driver
    config = ConfigParser()
    config.read(r'config.ini')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(config['params']['url'])
    request.cls.driver = driver
    request.cls.expectedTitle = config['params']['expectedTitle']
    yield
    driver.close()

