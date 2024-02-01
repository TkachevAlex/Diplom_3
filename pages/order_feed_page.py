from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import OrdersPageLocators
from pages.page import Page


class OrderFeedPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def open_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_ITEM)

    def get_history_orders(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrdersPageLocators.ALL_ORDERS_LIST))
        orders = [element.text.lstrip('#0') for element in
                  self.driver.find_elements(*OrdersPageLocators.ALL_ORDERS_LIST)]
        return orders

    def check_order_in_work(self, order):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(
                OrdersPageLocators.ORDER_IN_WORK, order))
            return True
        except TimeoutException:
            return False
