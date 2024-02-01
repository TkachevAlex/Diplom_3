from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators
from urls import Url


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def get_value_from_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def go_to_orders_feed_page(self):
        self.click_on_element(PageLocators.GO_TO_ORDERS_FEED_BTN)
        self.wait_load_url(Url.ORDERS_FEED_PAGE)

    def go_to_profile(self):
        self.click_on_element(PageLocators.GO_TO_PROFILE_BTN)
        self.wait_load_url(Url.PROFILE_PAGE)

    def go_to_login(self):
        self.click_on_element(PageLocators.GO_TO_PROFILE_BTN)
        self.wait_load_url(Url.LOGIN_PAGE)

    def go_to_main_page(self):
        self.click_on_element(PageLocators.GO_TO_CONSTRUCTOR_BTN)
        self.wait_load_url(Url.MAIN_PAGE)

    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def check_is_visible_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False




