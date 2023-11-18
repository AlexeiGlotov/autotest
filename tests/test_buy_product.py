from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from pages.filter_page import CFilter_page
from pages.product_page import CProduct_page
from pages.cart_page import CCart_page
import time

"""
Авторизация
Поиск товара 
Фильтрация по товару
Добавление товара в корзину
Работа в корзине
Оформление заказа

"""

def test_buy_product():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    action = ActionChains(driver)
    
    
    driver.get('https://www.vsempodarok.com')

    #Авторизация
    lp = Login_page(driver,action)
    lp.Authorization('x','x')

    #Применение фильтров
    fp = CFilter_page(driver,action)
    fp.install_filter()

    #Работа с товаром , добавление в корзину
    pp = CProduct_page(driver,action)
    pp.add_to_cart()
    
    #Работа в корзине , оформление заказа
    cp = CCart_page(driver,action)
    cp.go_to_order()

