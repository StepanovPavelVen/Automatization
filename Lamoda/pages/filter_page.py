import time
import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    click_filter_popularity = '//span[text()="По популярности"]'
    select_price_lower_on_popularity = '//span[text()="По убыванию цены"]'
    click_filter_price = '//span[text()="Цена"]'
    min_price = '//input[@name="minRange"]'
    max_price = '//input[@name="maxRange"]'
    accept = '//button[text()="Применить"]'

    # Getters
    def get_click_filter_popularity(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.click_filter_popularity)))

    def get_select_price_lower(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_price_lower_on_popularity)))

    def get_click_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_filter_price)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_accept(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept)))

    def get_price_product(self):
        time.sleep(2)
        price_product = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class = "x-product-card-description__price-single x-product-card-description__price-WEB8507_price_no_bold _price_k0rqx_8"]')))
        text_price_product = price_product.text
        return text_price_product

    # Actions
    def click_popularity(self):
        self.driver.execute_script("arguments[0].click()", self.get_click_filter_popularity())

    def click_select_price_lower(self):
        self.get_select_price_lower().click()
        print('Выбрана сортировка по "Убыванию цены"')
        time.sleep(2)

    def click_price(self):
        self.get_click_filter_price().click()


    def input_price(self, min, max):
        self.get_price_min().send_keys(min)
        self.get_price_max().send_keys(Keys.BACKSPACE * 10)
        self.get_price_max().send_keys(max)
        self.get_accept().click()
        print('Отсортированно по цене (78 800 рублей)')


    # Methods
    def filter(self):
        with allure.step('Filter'):
            Logger.add_start_step(method="filter")
            self.click_popularity()
            self.click_select_price_lower()
            self.get_most_expensive_product()
            self.click_price()
            self.input_price(78800, 78800)
            Logger.add_end_step(url=self.driver.current_url, method="filter")
