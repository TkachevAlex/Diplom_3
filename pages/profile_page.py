from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfilePageLocators
from pages.page import Page


class ProfilePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_orders_history(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BTN)

    def logout(self):
        self.click_on_element(ProfilePageLocators.EXIT_BTN)

    def get_history_orders(self):
        self.go_to_orders_history()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.ORDERS_HISTORY_LIST))
        orders = [element.text.lstrip('#0') for element in self.driver.find_elements(*ProfilePageLocators.ORDERS_HISTORY_LIST)]
        return orders
