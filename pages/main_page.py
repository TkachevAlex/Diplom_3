from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from pages.page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.order = None

    def add_ingredient_in_basket(self, element):
        element = self.driver.find_element(*element)
        target = self.driver.find_element(*MainPageLocators.BASKET_AREA)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def create_order(self):
        self.add_ingredient_in_basket(element=MainPageLocators.INGREDIENT)
        self.click_on_element(MainPageLocators.CREATE_ORDER)
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element((MainPageLocators.ORDER_NUMBER), "9999"))
        self.order = self.get_value_from_element(MainPageLocators.ORDER_NUMBER)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW)
        return self.order