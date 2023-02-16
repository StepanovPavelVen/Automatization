import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    '''Метод открытия главной страницы ламода на мужском разделе'''

    def open_lamoda_man(self):
        self.driver.get('https://www.lamoda.ru/men-home/?sitelink=topmenuM')
        self.driver.maximize_window()

    '''Метод получения текущего url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Текущий URL: ' + get_url)

    """Метод получения самого дорогого товара на странице"""

    def get_most_expensive_product(self):
        expensive_product = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="x-product-card__link x-product-card__hit-area"]')))
        text_expensive_product = expensive_product.text
        print('Самый дорогой товар:\n' + text_expensive_product)

    """Метод screenshot"""

    def screenshot(self):
        date_screenshot = datetime.datetime.utcnow().strftime('%d.%m.%Y.%H.%M.%S')
        name_screenshot = 'Screenshot' + date_screenshot + '.png'
        self.driver.save_screenshot('./screen/' + name_screenshot)

    '''Метод assert URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print ('Открыта нужная страница')


    '''Assert price'''
    def assert_price(self):
        assert self.get_price_product() == self.get_price_product_in_cart()
        print('Цены совпадают')


