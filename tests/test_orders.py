import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


class TestOrders:

    @allure.title('Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_detail_window(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed_page()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order()
        assert order_feed_page.check_visible_order_window()

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_in_orders_history_is_on_order_feed_page(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        user_orders = profile_page.get_history_orders()
        profile_page.go_to_orders_feed_page()

        order_feed_page = OrderFeedPage(driver)
        all_orders = order_feed_page.get_history_orders()
        assert set(user_orders) <= set(all_orders)

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_all_orders_increment(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed_page()

        order_page = OrderFeedPage(driver)
        all_orders_before = order_page.get_all_orders_count()
        order_page.go_to_main_page()

        main_page.create_order()
        main_page.go_to_orders_feed_page()

        all_orders_after = order_page.get_all_orders_count()
        assert int(all_orders_before) < int(all_orders_after)

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_today_orders_increment(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed_page()

        order_page = OrderFeedPage(driver)
        today_orders_before = order_page.get_today_orders_count()
        order_page.go_to_main_page()

        main_page.create_order()
        main_page.go_to_orders_feed_page()

        today_orders_after = order_page.get_today_orders_count()
        assert int(today_orders_before) < int(today_orders_after)

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_is_order_in_work(self, driver, login_user):
        main_page = MainPage(driver)
        order = main_page.create_order()
        main_page.go_to_orders_feed_page()

        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.check_order_in_work(order)