import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вернуть текущий Url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Дождаться ожидаемого Url')
    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Найти элемент')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Найти все элементы')
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def drag_and_drop(self, element, target):
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Подождать появления элемента')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Подождать появления текста в элементe')
    def wait_show_text_in_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False


    @allure.step('Подождать исчезновения текста в элементe')
    def wait_hide_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Вернуть text элемента')
    def get_value_from_element(self, locator):
        self.wait_element(locator)
        return self.get_element(locator).text

    @allure.step('Вернуть аттрибут элемента')
    def get_attribute_from_element(self, locator, attribute):
        self.wait_element(locator)
        return self.get_element(locator).get_attribute(attribute)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.wait_element(locator)
        self.get_element(locator).click()

    @allure.step('Ввести текст в элемент')
    def enter_text_in_element(self, locator, text):
        self.wait_element(locator)
        self.get_element(locator).send_keys(text)

    @allure.step('Проверить видимость элемента')
    def check_is_visible_element(self, locator):
        try:
            self.wait_element(locator)
            return True
        except TimeoutException:
            return False

