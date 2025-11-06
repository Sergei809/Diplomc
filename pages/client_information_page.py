# Страница ввода данных клиента
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Импортируем базовый класс
from base.base_class import Base
class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    email = "//input[@id='email']"
    first_name = "//input[@placeholder='First name']"
    last_name = "//input[@placeholder='Last name']"
    address = "//input[@placeholder='Address']"
    apartment = "//input[@placeholder='Apartment, suite, etc. (optional)']"
    city = "//input[@placeholder='City']"
    postal_code = "//input[@placeholder='Postal code']"
    phone = "//input[@placeholder='Phone']"
    cart_number = "//input[@placeholder='Card number']"
    cart_expiration = "//input[@placeholder='Expiration date (MM / YY)']"
    cart_securetycod = "//input[@placeholder='Security code']"
    name_on_card = "//input[@placeholder='Name on card']"
    checkoutpay_button = "//button[@id='checkout-pay-button']"

    # Getters
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    
    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))
    
    def get_apartment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apartment)))
    
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))
    
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    
    def get_cart_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_number)))
    
    def get_cart_expiration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_expiration)))
    
    def get_cart_securetycod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_securetycod)))
    
    def get_name_on_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_on_card)))
    
    def get_checkoutpay_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkoutpay_button)))

    # Actions
    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Input address")

    def input_apartment(self, apartment):
        self.get_apartment().send_keys(apartment)
        print("Input apartment")

    def input_city(self, city):
        self.get_city().send_keys(city)
        print("Input city")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal_code")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    # Поля для оплаты вынесены отдельно. Работа с элементами внутри iframe
    def input_cart_number(self, cart_number):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title*="Card number"], iframe[name*="card-fields-number"], iframe[src*="card-fields"]'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="cc-number"], input[name*="number"]'))
            ).send_keys(cart_number)
            print("Input cart_number")
        finally:
            self.driver.switch_to.default_content()

    def input_cart_expiration(self, cart_expiration):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title*="Expiration"], iframe[name*="card-fields-expiry"], iframe[src*="card-fields"]'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="cc-exp"], input[name*="expiry"]'))
            ).send_keys(cart_expiration)
            print("Input cart_expiration")
        finally:
            self.driver.switch_to.default_content()

    def input_cart_securetycod(self, cart_securetycod):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title*="Security code"], iframe[name*="card-fields-verification"], iframe[src*="card-fields"]'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="cc-csc"], input[name*="verification"]'))
            ).send_keys(cart_securetycod)
            print("Input cart_securetycod")
        finally:
            self.driver.switch_to.default_content()

    def input_name_on_card(self, name_on_card):
        found = False
        try:
            el = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="cc-name"], input[name*="name"]'))
            )
            el.send_keys(name_on_card)
            found = True
            print("Input name_on_card (main)")
        except Exception:
            pass
        
        if not found:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title*="Name"], iframe[src*="card-fields"], iframe[name*="card-fields"]'))
                )
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="cc-name"], input[name*="name"]'))
                ).send_keys(name_on_card)
                found = True
                print("Input name_on_card (iframe)")
            finally:
                self.driver.switch_to.default_content()
        
        if not found:
            raise TimeoutException("Name on card field not found in main DOM or iframe")

    def click_checkoutpay_button(self):
        # Скрываем всплывающие элементы перед кликом
        try:
            self.driver.execute_script("""
                var elements = document.querySelectorAll('shopify-forms-embed');
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }
            """)
            print("Всплывающие элементы скрыты перед кликом на кнопку оплаты")
        except Exception as e:
            print(f"Не удалось скрыть всплывающие элементы: {e}")
        
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkoutpay_button)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        print("Click checkoutpay_button via JavaScript")

    # Methods
    def input_information(self):
        # Вызываем методы
        self.get_current_url()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
        self.input_email('gm.sergei.beliaev@gmail.com')
        self.input_first_name('firstname')
        self.input_last_name('lastname')
        self.input_address('123 Main St')
        self.input_apartment('apartment')
        self.input_city('Tokio')
        self.input_postal_code('ABC 1234')
        self.input_phone('+81 3 1234 5678')
        self.input_cart_number('1234567890123456')
        self.input_cart_expiration('12/25')
        self.input_cart_securetycod('123')
        self.input_name_on_card('Jason Smith')
        # self.click_checkoutpay_button() - специально не использую, чтобы не оплачивать заказ