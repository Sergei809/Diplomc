import datetime

# Создаем базовый класс
class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert words"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # делаем скриншот
    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + '.png'
        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\Diplom\\screen\\' + name_screenshot)

    # Проверка url
    """Method url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
