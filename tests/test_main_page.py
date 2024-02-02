import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import Url


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed_page()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_main_page()
        assert main_page.get_url() == Url.MAIN_PAGE

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_go_to_orders_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed_page()
        assert main_page.get_url() == Url.ORDERS_FEED_PAGE

    @allure.title('Проверка, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.view_ingredient()
        assert main_page.check_visible_ingredient_detail_windows()

    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    def test_close_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.view_ingredient()
        main_page.close_ingredient_detail_windows()
        assert not main_page.check_visible_ingredient_detail_windows()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increment_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_value = main_page.get_ingredient_count()
        print(start_value)
        main_page.add_ingredient_in_basket()
        finish_value = main_page.get_ingredient_count()
        print(finish_value)
        assert int(start_value) < int(finish_value)

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_create_order_authorized_user(self, driver, login_user):
        main_page = MainPage(driver)
        order = main_page.create_order()
        assert order
