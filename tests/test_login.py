from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, AuthLogin, AuthPassword
from data.urls import Urls

class TestStellarBurgersLoginLogoutForm:

    # 1. Тест: при вводе корректных данных отображается основная страница через прямую авторизацию
    def test_login_correct_email_and_password_show_main_page(self, login):
        assert login.current_url == Urls.url_main_page
        
        assert WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(MainPage.mn_order_button)
        ).is_displayed(), "Кнопка 'Оформить заказ' не отображается на главной странице"

    # 2. Вход через кнопку "Войти в аккаунт" на главной
    def test_login_sign_in_button_show_login_page(self, driver):
        driver.get(Urls.url_main_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.mn_auth)).click()
        
        # Проверяем, что URL изменился
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))

    # 3. Вход через кнопку "Личный Кабинет" на главной
    def test_login_personal_account_button_show_login_page(self, driver):
        driver.get(Urls.url_main_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.mn_profile_button)).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))

    # 4. Вход через форму регистрации
    def test_login_registration_form_sign_in_button(self, driver):
        driver.get(Urls.url_register)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLogin.al_login_text_with_href)).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))

    # 5. Вход через форму восстановления пароля
    def test_login_forgot_password_form_sign_in_button(self, driver):
        driver.get(Urls.url_forgot_password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPassword.ap_login_text_with_href)).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))
