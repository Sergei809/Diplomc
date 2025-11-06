# Страница выбора товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импортируем базовый класс
from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_product_1 = "//img[@alt='Crewneck Sweatshirt Ebroidery Logo']"
    select_product_1_link = "//a[.//img[@alt='Crewneck Sweatshirt Ebroidery Logo']]"
    cart = "//div[@id='cart-icon']"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    
    def get_select_product_1_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1_link)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

     # Actions

    def click_select_product_1(self):
        # Пытаемся найти ссылку товара, если не найдем - используем изображение через JavaScript
        try:
            element = self.get_select_product_1_link()
            print("Найдена ссылка товара через XPath")
        except:
            # Если не нашли ссылку, пытаемся найти родительский элемент через JavaScript
            img_element = self.get_select_product_1()
            element = self.driver.execute_script("""
                var img = arguments[0];
                var link = img.closest('a');
                return link || img;
            """, img_element)
            print("Использован родительский элемент через JavaScript")
        
        # Кликаем по элементу
        self.driver.execute_script("arguments[0].click();", element)
        print("Click select_product_1 via JavaScript")

    def click_cart(self):
        # Скрываем всплывающие элементы перед кликом
        try:
            self.driver.execute_script("""
                var elements = document.querySelectorAll('shopify-forms-embed');
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }
            """)
            print("Всплывающие элементы скрыты перед кликом на корзину")
        except Exception as e:
            print(f"Не удалось скрыть всплывающие элементы: {e}")
        
        element = self.get_cart()
        # Используем JavaScript клик, так как элемент может быть перекрыт
        self.driver.execute_script("arguments[0].click();", element)
        print("Click cart via JavaScript")

    # Methods
    # Для теста test_bue_product
    def select_select_men(self):
        # Вызываем методы
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_1(self):
        # Вызываем методы
        self.get_current_url()
        
        # Ждем загрузки страницы с товарами
        print("Ожидание загрузки товаров...")
        time.sleep(3)  # Даем время на загрузку товаров
        
        # Проверяем, что мы на правильной странице
        current_url = self.driver.current_url
        print(f"Текущий URL: {current_url}")
        
        # Пытаемся найти товар
        try:
            self.click_select_product_1()
            print("Товар успешно выбран")
            # Ждем перехода на страницу товара
            time.sleep(3)
            # Проверяем, что перешли на страницу товара
            new_url = self.driver.current_url
            print(f"URL после выбора товара: {new_url}")
        except Exception as e:
            print(f"Ошибка при выборе товара: {e}")
            # Делаем скриншот для отладки
            self.get_screenshot()
            raise

