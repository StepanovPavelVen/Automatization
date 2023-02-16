from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Man_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    man_clothes_page = '//a[@href="/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=3"]'
    man_shoes_page = '//a[@href="/c/17/shoes-men/?sitelink=topmenuM&l=4"]'
    man_accessories_page = '//a[@href="/c/559/accs-muzhskieaksessuary/?sitelink=topmenuM&l=5"]'

    # Getters
    def get_man_clothes_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.man_clothes_page)))

    def get_shoes_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.man_shoes_page)))

    def get_accessories_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.man_accessories_page)))

    # Actions
    def click_man_clothes_page(self):
        self.get_man_clothes_page().click()
        print('Открыт сайт на главной мужской странице')

    def click_man_shoes_page(self):
        self.get_shoes_page().click()

    def click_accessories_page(self):
        self.get_accessories_page().click()

    # Methods
    def open_man_clothes_page(self):
        self.open_lamoda_man()
        self.click_man_clothes_page()
        self.get_current_url()
        self.assert_url('https://www.lamoda.ru/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=3')

    # def open_man_shoes_page(self):
    #     self.open_lamoda_man()
    #     self.click_man_shoes_page()
    #
    # def open_accessories_page(self):
    #     self.open_lamoda_man()
    #     self.click_accessories_page()
