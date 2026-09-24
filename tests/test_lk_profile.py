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
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_profile))

    # Переход в конструктор через кнопку «Конструктор»
    def test_click_constructor_button_show_constructor_form(self, open_profile):
        driver = open_profile
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.mn_constructor_button)).click()
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPage.mn_constructor_header, "Соберите бургер")
        )

    # Переход в конструктор через логотип
    def test_click_logo_button_show_constructor_form(self, open_profile):
        driver = open_profile
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.mn_logo)).click()
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPage.mn_constructor_header, "Соберите бургер")
        )

    # Выйти из аккаунта
    def test_click_logout_button_in_lk_open_login_form(self, open_profile):
        driver = open_profile
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LKProfile.lk_logout_button)).click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLogin.al_login_button_any_forms))
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))
