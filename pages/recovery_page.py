from locators import RecoveryPageLocators
from pages.page import Page


class RecoveryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def filling_recovery_form(self, user_data):
        self.driver.find_element(*RecoveryPageLocators.EMAIL_INPUT).send_keys(user_data['email'])
        self.driver.find_element(*RecoveryPageLocators.SUBMIT_BUTTON).click()
