from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from pages.Select_product_man_clothes import Select_product_page
from pages.cart_page import Cart_page
from pages.filter_page import Filter_page
from pages.man_page import Man_page
from pages.user_page import User_page
from utilities.logger import Logger


@allure.description('Test buy product')
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/pavel/PycharmProjects/resource/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    print('\nStart test')

    open_man_clothes = Man_page(driver)
    open_man_clothes.open_man_clothes_page()

    fp = Filter_page(driver)
    fp.filter()
    get_price = fp.get_price_product()

    buy_product = Select_product_page(driver)
    buy_product.buy_product()

    cp = Cart_page(driver)
    Logger.add_start_step(method="assert price = price_in_cart")
    get_price_in_cart = cp.get_price_product_in_cart()
    assert get_price == get_price_in_cart
    print('Цена товра = цене товара в корзине')
    Logger.add_end_step(url=driver.current_url, method="assert price = price_in_cart")
    cp.cart_page_next()

    up = User_page(driver)
    Logger.add_start_step(method="assert price = price_in_user_page")
    get_price_in_user_page = up.get_price_product_in_user_page()
    assert get_price == get_price_in_user_page
    print('Цена товра = цене товара на странице оформления заказа')
    Logger.add_end_step(url=driver.current_url, method="assert price = price_in_user_page")
    up.input_information_user()

    print('Finish test')
    driver.quit()