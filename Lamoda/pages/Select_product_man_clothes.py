import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Select_product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product = '//img[@src="//a.lmcdn.ru/img389x562/M/P/MP002XM093YA_18907385_1_v1_2x.jpg"]'
    menu_select_size = '//div[text()="Выберите размер"]'
    select_size = '//div[text()="58 RUS"]'
    add_product_to_cart = '//span[text()="Добавить в корзину"]'
    go_to_cart = '//a[text()="Перейти в корзину"]'

    # Getters
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_menu_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_select_size)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_add_product_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions
    def click_product(self):
        self.driver.execute_script("arguments[0].click()", self.get_product())
        print('Выбран продукт отсортированный по цене')

    def click_menu_select_size(self):
        self.get_menu_select_size().click()

    def click_select_size(self):
        self.driver.execute_script("arguments[0].click()", self.get_select_size())
        print('Выбран размер')

    def click_add_product_to_cart(self):
        self.driver.execute_script("arguments[0].click()", self.get_add_product_to_cart())
        print('Товар добавлен в корзину')

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('Перешли в корзину')

    # Methods
    def buy_product(self):
        self.click_product()
        self.get_current_url()
        self.assert_url('https://www.lamoda.ru/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=3&sort=price_desc&price=78800%2C78800')
        time.sleep(2)
        self.screenshot()
        self.click_menu_select_size()
        self.click_select_size()
        self.click_add_product_to_cart()
        self.click_go_to_cart()

