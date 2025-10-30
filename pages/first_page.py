# Главная страница

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# Для явного ожидания:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импортируем базовый класс
from base.base_class import Base


class First_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_men = "//details[@id='Details-HeaderMenu-1']"
    men_link = "//a[contains(@href, '/collections/men')]"
    men_link_alt = "//a[contains(text(), 'Men')]"

    # Getters
    def get_select_men(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_men)))
    
    def get_men_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.men_link)))

    # Actions
    # Эот элемент у меня перекрывается, использую конструкцию с avascript
    def click_select_men(self):
        element = self.get_select_men()
        self.driver.execute_script("arguments[0].click();", element)
        print("Click select_men via JavaScript")
    
    def click_men_link(self):
        self.get_men_link().click()
        print("Click men_link")

    # Methods
    # Для теста test_bue_product
    def select_select_mens(self):
        # Вызываем методы
        self.get_current_url()
        
        # Переходим напрямую на страницу с товарами для мужчин
        men_url = "https://hudsonstore.com/collections/men"
        self.driver.get(men_url)
        print(f"Переход на страницу: {men_url}")
        
        # Ждем загрузки страницы
        time.sleep(3)
        
        # Проверяем текущий URL
        current_url = self.driver.current_url
        print(f"URL после перехода на страницу Men: {current_url}")


