import pytest
from selenium import webdriver
import utils
import requests
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import Url


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    if 'chrome' in browser.lower():
        driver = webdriver.Chrome()
    elif 'firefox' in browser.lower():
        driver = webdriver.Firefox()
    else:
        raise ValueError('Указан неверный браузер')
    driver.maximize_window()
    driver.get(Url.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture()
def user_data():
    user_data = utils.generate_user_data()
    response = requests.post(Url.MAIN_PAGE + Url.CREATE_USER_ENDPOINT, user_data)
    yield user_data
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(Url.MAIN_PAGE + Url.DELETE_USER_ENDPOINT, headers=headers)


@pytest.fixture()
def login_user(driver, user_data):
    MainPage(driver).enter_in_account()
    LoginPage(driver).login_user(user_data)