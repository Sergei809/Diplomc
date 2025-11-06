# Страница корзины

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Импортируем базовый класс
from base.base_class import Base
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_securely_button = "//button[@name='checkout']"

    # Getters
    def get_checkout_securely_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_securely_button)))

    # Actions
    def click_checkout_securely_button(self):
        max_tries = 3
        last_exception = None
        for attempt in range(max_tries):
            try:
                # Получаем элемент непосредственно перед каждым действием — для защиты от StaleElementReferenceException
                element = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, self.checkout_securely_button))
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                self.driver.execute_script("arguments[0].click();", element)
                print(f"Click checkout_securely_button via JavaScript (try {attempt + 1})")
                # Ожидание смены URL (оформление заказа)
                WebDriverWait(self.driver, 10).until(lambda d: "checkout" in d.current_url or "order" in d.current_url)
                return
            except Exception as e:
                print(f"Попытка {attempt+1}: {type(e).__name__} — {e}")
                last_exception = e
        print(f"Не удалось кликнуть по checkout_securely_button после {max_tries} попыток")
        if last_exception:
            raise last_exception

    # Methods
    def product_confirmation(self):
        # Вызываем методы
        self.get_current_url()
        self.click_checkout_securely_button()

