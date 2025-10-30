# модуль авторизации
# gm.sergei.beliaev@gmail.com
# fortest09477$R

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Импортируем базовый класс
from base.base_class import Base


class Login_page(Base):
    # URL
    url = 'https://hudsonstore.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    account_login = "//li[@class='hidden lg:block']"
    user_name = "//input[@id='CustomerEmail']"
    password = "//input[@id='CustomerPassword']"
    button_login = "//input[@value='Log In']"
    main_word = "//img[@alt='Hudson Store | Online Shopping']"

    # Getters
    def get_account_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_login)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.main_word)))

    # Actions
    def click_account_login(self):
        element = self.get_account_login()
        self.driver.execute_script("arguments[0].click();", element)
        print("Клик account_login via JavaScript")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))  # Жду появления поля логина

    def input_user_name(self, user_name):
        # Очищаем поле перед вводом
        user_field = self.get_user_name()
        user_field.clear()
        user_field.send_keys(user_name)
        print("Введен user_name")

    def input_password(self, password):
        # Очищаем поле перед вводом
        pass_field = self.get_password()
        pass_field.clear()
        pass_field.send_keys(password)
        print("Введен password")

    def click_button_login(self):
        # Скрываем всплывающие элементы перед кликом
        try:
            self.driver.execute_script("""
                var elements = document.querySelectorAll('shopify-forms-embed');
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }
            """)
            print("Всплывающие элементы скрыты перед кликом на кнопку логина")
        except Exception as e:
            print(f"Не удалось скрыть всплывающие элементы: {e}")
        element = self.get_button_login()
        self.driver.execute_script("arguments[0].click();", element)
        print("Клик button_login via JavaScript")
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.main_word)))

    # Methods
    def authorization(self):
        # Переходим на главную страницу
        self.driver.get(self.url)
        print(f"Переход на страницу: {self.url}")

        # Ждем полной загрузки страницы
        WebDriverWait(self.driver, 30).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")
        # Максимизируем окно
        self.driver.maximize_window()

        # Вызываем методы
        self.get_current_url()


