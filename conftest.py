import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from data.urls import Urls
from data.data import PersonData



@pytest.fixture(scope='function')
# Привязка браузера
def driver():
    options = Options()
    options.add_argument("--start-maximized") # развернем на весь экран
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture
# Войти в аккаунт 
def login(driver):
    driver.get(Urls.url_login)    
    # Ожидаем форму и заполняем данные
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLogin.al_email_field)).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)
    
    # Кликаем "Войти"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLogin.al_login_button_any_forms)).click()
    
    # Ждем загрузки главной страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.mn_order_button))
    return driver

# Автоматически открывает Личный кабинет перед тестом
@pytest.fixture
def open_profile(login):
    driver = login
    driver.find_element(*MainPage.mn_profile_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LKProfile.lk_info_message))
    return driver