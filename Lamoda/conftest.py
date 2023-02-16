import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/pavel/PycharmProjects/resource/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)
    driver.get('https://www.lamoda.ru/men-home/?sitelink=topmenuM')
    driver.maximize_window()
    yield
    driver.quit()
