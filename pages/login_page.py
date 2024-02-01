from locators import LoginPageLocators, MainPageLocators
from pages.page import Page
from urls import Url


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self, user_data):
        self.click_on_element(MainPageLocators.ENTER_IN_ACCOUNT)
        self.wait_load_url(Url.LOGIN_PAGE)
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_data['email'])
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data['password'])
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        self.wait_load_url(Url.MAIN_PAGE)

    def go_to_recovery_password(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD)

    def check_active_field(self, locator):
        if 'status_active' in self.driver.find_element(*locator).get_attribute('class'):
            return True
        else:
            return False
