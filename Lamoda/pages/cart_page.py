import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.Select_product_man_clothes import Select_product_page
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    go_to_user_page = '//span[text()="Перейти к оформлению"]'
    price_product_in_cart = '//span[@discount="false"]'

    # Getters
    def get_go_user_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_user_page)))

    def get_price_product_in_cart(self):
        price_product_in_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@discount="false"]')))
        text_price_product_in_cart = price_product_in_cart.text
        return text_price_product_in_cart

    # Actions
    def click_go_user_cart(self):
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.get_go_user_cart())
        print('Переход к оформлению заказа')

    # Methods
    def cart_page_next(self):
        with allure.step('Go to user page'):
            Logger.add_start_step(method="cart_page_next")
            time.sleep(2)
            self.screenshot()
            self.click_go_user_cart()
            Logger.add_end_step(url=self.driver.current_url, method="cart_page_next")
