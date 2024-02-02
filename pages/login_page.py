import allure
from locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Url


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на Показать/Скрыть пароль')
    def hide_or_show_password(self):
        self.click_on_element(LoginPageLocators.SHOW_PASSWORD)

    @allure.step('Авторизоваться пользователем')
    def login_user(self, user_data):
        self.wait_load_url(Url.LOGIN_PAGE)
        self.enter_text_in_element(LoginPageLocators.EMAIL_INPUT, user_data['email'])
        self.enter_text_in_element(LoginPageLocators.PASSWORD_INPUT, user_data['password'])
        self.click_on_element(LoginPageLocators.SUBMIT_BUTTON)
        self.wait_load_url(Url.MAIN_PAGE)

    @allure.step('Перейти на страницу Восстановление пароля')
    def go_to_recovery_password(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD)

    @allure.step('Проверить активность поля')
    def check_active_password_field(self):
        if 'status_active' in self.get_attribute_from_element(LoginPageLocators.PASSWORD_CONTAINER, 'class'):
            return True
        else:
            return False

    @allure.step('Проверить видимость формы авторизации')
    def check_visible_login_form(self):
        return self.check_is_visible_element(LoginPageLocators.LOGIN_FORM)
