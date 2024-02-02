import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_user_profile(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        assert profile_page.check_visible_profile_info()

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_story_order(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.go_to_orders_history()
        assert profile_page.check_visible_order_history()

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_profile(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.logout()

        login_page = LoginPage(driver)
        assert login_page.check_visible_login_form()
