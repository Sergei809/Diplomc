"""Это тест, в который импортируем модуль авторизации (login_page)"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импортируем класс авторизации из модуля авторизации, учитывая директорию pages
from pages.login_page import Login_page
from pages.first_page import First_page
from pages.main_page import Main_page
from pages.add_cart_page import Add_cart_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page

@pytest.mark.run(order=1)
def test_buy_product_1():
    # Подключаем браузер
    firefox_options = Options()
    #firefox_options.add_argument("--headless") #тогл включения headless
    driver = webdriver.Firefox(options=firefox_options)
    print("Start test 1")

# Прописываем переменные
    login = Login_page(driver)
    login.authorization()

    fp = First_page(driver)
    fp.select_select_mens()

    mp = Main_page(driver)
    mp.select_products_1()

    ac = Add_cart_page(driver)
    ac.add_cart_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    print("Finish test 1")
    time.sleep(10)
    # driver.quit()  # Браузер не закрывается для проверки результата

# Запуск всех файлов тестов python -m pytest -s -v test_buy_product.py
# Запуск файла теста python -m pytest -s -v (test_buy_product.py)
# Запуск только одного теста python -m pytest -s -v -k (test_buy_product_3)
# Чтобы тесты выполнить в доп указанном порядке, не забыть установить pip install pytest-ordering
