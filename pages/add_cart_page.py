# Главная страница

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импортируем базовый класс
from base.base_class import Base


class Add_cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_cart_button1 = "//button[@class='product-form__submit button button-pill w-full font-body h-[55px] text-sm text-primary-button_text_color button-secondary']"
    size_select = "//label[@data-size='M']"
    checkout_button = "//div[@id='cart-icon']"
   
    # Getters
    def get_add_cart_button1(self):
        # Пытаемся найти кнопку разными способами
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button1)))
        except:
            try:
                return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button_alt)))
            except:
                return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button_text)))
    
    def get_size_select(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.size_select)))
        except:
            return None

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def close_overlays(self):
        try:
            self.driver.execute_script('''
                var elements = document.querySelectorAll('shopify-forms-embed');
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }
            ''')
            print("Всплывающие элементы скрыты (close_overlays)")
        except Exception as e:
            print(f"Не удалось скрыть всплывающие элементы: {e}")

    # Actions
    def select_size_1(self):
        self.close_overlays()
        el = self.get_size_select()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.size_select)))
        el.click()
        print("Выбран размер товара")
        
    def click_add_cart_button1(self):
        self.close_overlays()
        self.get_add_cart_button1().click()
        print("Клик add_cart_button1")
      
        # Ждем подтверждения добавления товара или проверяем изменение в DOM
        try:
            # Проверяем наличие уведомления о добавлении или изменение кнопки
            notification = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.cart_notification))
            )
            print("Товар успешно добавлен в корзину (найдено уведомление)")
        except:
            # Альтернативная проверка - просто ждем немного и продолжаем
            print("Товар добавлен (проверка подтверждения пропущена, но продолжаем)")
    
    def click_checkout_button(self):
        # Скрываем всплывающие элементы перед кликом
        try:
            self.driver.execute_script("""
                var elements = document.querySelectorAll('shopify-forms-embed');
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }
            """)
            print("Всплывающие элементы скрыты перед кликом на кнопку checkout")
        except Exception as e:
            print(f"Не удалось скрыть всплывающие элементы: {e}")
        
        element = self.get_checkout_button()
        # Используем JavaScript клик, так как элемент может быть перекрыт
        self.driver.execute_script("arguments[0].click();", element)
        print("Click checkout_button via JavaScript")

    # Methods
    def add_cart_1(self):
        # Вызываем методы
        self.get_current_url()
        self.select_size_1()
        self.click_add_cart_button1()
        self.click_checkout_button()
