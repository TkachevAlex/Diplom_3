import allure
from locators import MainPageLocators
from pages.main_page import MainPage
from urls import Url


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_main_page(self, driver):
        page = MainPage(driver)
        page.go_to_orders_feed_page()
        page.go_to_main_page()
        assert page.get_url() == Url.MAIN_PAGE

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_go_to_orders_page(self, driver):
        page = MainPage(driver)
        page.go_to_orders_feed_page()
        assert page.get_url() == Url.ORDERS_FEED_PAGE

    @allure.title('Проверка, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.INGREDIENT)
        assert main_page.check_is_visible_element(MainPageLocators.MODAL_WINDOW)

    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    def test_close_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.INGREDIENT)
        main_page.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW)
        assert not main_page.check_is_visible_element(MainPageLocators.MODAL_WINDOW)

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингрtдиента увеличивается')
    def test_increment_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_value = main_page.get_value_from_element(MainPageLocators.INGREDIENT_COUNTER)
        main_page.add_ingredient_in_basket(element=MainPageLocators.INGREDIENT)
        finish_value = main_page.get_value_from_element(MainPageLocators.INGREDIENT_COUNTER)
        assert int(start_value) < int(finish_value)

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_create_order_authorized_user(self, driver, login_user):
        main_page = MainPage(driver)
        order = main_page.create_order()
        assert order
