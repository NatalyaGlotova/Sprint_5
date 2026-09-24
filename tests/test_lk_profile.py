from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LKProfile, MainPage, AuthLogin
from data.urls import Urls

class TestStellarBurgersProfileForm:
    
    # Открыть Личный кабинет
    def test_click_profile_button_open_profile_form(self, open_profile):
        driver = open_profile
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LKProfile.lk_history_shop_button))
        assert driver.current_url == Urls.url_profile

    # Переход в конструктор через кнопку «Конструктор»
    def test_click_constructor_button_show_constructor_form(self, open_profile):
        driver = open_profile
        driver.find_element(*MainPage.mn_constructor_button).click()
        h1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//h1")))
        assert h1.text == "Соберите бургер"

    # Переход в конструктор через логотип
    def test_click_logo_button_show_constructor_form(self, open_profile):
        driver = open_profile
        driver.find_element(*MainPage.mn_logo).click()
        h1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//h1")))
        assert h1.text == "Соберите бургер"

    # Выйти из аккаунта
    def test_click_logout_button_in_lk_open_login_form(self, open_profile):
        driver = open_profile
        driver.find_element(*LKProfile.lk_logout_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLogin.al_login_button_any_forms))
        assert driver.current_url == Urls.url_login
