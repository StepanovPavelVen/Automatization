import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class User_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    location = '//input[@id="city_name"]'
    click_pickup = '//span[text()="Самовывоз"]'
    button_pick_up = '//button[text()="Выбрать пункт самовывоза"]'
    pickup_point = '//div[text()="Революционная, 107"]'
    select_pickup_point = '//button[@class="x-button x-button_primaryFilledWeb7184 x-button_32 _submit_198zj_85"]'
    first_name = '//input[@id="first_name"]'
    last_name = '//input[@id="last_name"]'
    phone = '//input[@id="phone"]'
    email = '//input[@id="email"]'
    done = '//span[text()="Оформить заказ"]'

    # Getters
    def get_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location)))

    def get_click_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_pickup)))

    def get_button_pick_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pick_up)))

    def get_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_point)))

    def get_select_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pickup_point)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_done(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.done)))

    # Actions
                # Ламода подставляет город автоматически. Чтобы у вас сработал тест надо убрать комментарии с блока кода ниже. Я закоментировал потому что ARROW DOWN не работает на MAC OS
                #У ламоды баг. При попытке вставить город поле работает некорректно. Поэтому выход только такой. Спасибо за понимание
    # def input_location(self):
    #     self.get_location().send_keys(Keys.BACKSPACE * 100)
    #     self.get_location().send_keys('г. Уфа')
    #     self.get_location().send_keys(Keys.ARROW_DOWN)
    #     self.get_location().send_keys(Keys.RETURN)

    def click_samovyvoz(self):
        self.get_click_pickup().click()
        print('Выбран способ получения "Самовывоз"')

    def select_pick_up(self):
        self.get_button_pick_up().click()

    def click_pickup_point(self):
        self.get_pickup_point().click()
        print('Выбран адрес пункта самовывоза')

    def click_select_pickup_point(self):
        self.get_select_pickup_point().click()
        print('Пункт самовывоза выбран')

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Ввод Имени')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Ввод Фамилии')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('Ввод Телефона')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Ввод email')

    def click_done(self):
        self.get_done().click()
        time.sleep(2)
        self.get_done().click()
        print('Заказ оформлен')

    # Methods
    def input_information_user(self):
        self.get_current_url()
        self.assert_url('https://www.lamoda.ru/checkout/cart/')
        # self.input_location() Тоже снять комментарий!
        self.click_samovyvoz()
        self.select_pick_up()
        self.click_pickup_point()
        self.click_select_pickup_point()
        self.input_first_name('Иван')
        self.input_last_name('Иванов')
        self.input_phone(1111111111)
        self.input_email('test@ya.ru')
        self.click_done()
        time.sleep(2)
        self.screenshot()



