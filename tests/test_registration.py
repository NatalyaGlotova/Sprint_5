import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import AuthRegistre, AuthLogin

from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:
    # Вспомогательный метод для безопасного поиска списка элементов с ожиданием
    def _wait_for_elements(self, driver, locator, timeout=5):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    # При успешной регистрации перебрасывает на страницу входа
    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        user_data = ValidData()
        driver.get(Urls.url_register)
        
        driver.find_element(*AuthRegistre.ar_name_field).send_keys(user_data.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(user_data.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(user_data.password)

        # Ждем, пока кнопка регистрации точно станет доступна для клика
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button)
        )
        register_button.click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.url_login))
        
        login_elements = self._wait_for_elements(driver, AuthLogin.al_element_with_login_text)
        
        assert len(login_elements) > 0 and login_elements[0].is_displayed()

    # При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет
    def test_registration_empty_name_nothing_happens(self, driver):
        driver.get(Urls.url_register)
        
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('GlotovaNatalya55@yandex.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('1478963qaz')
        
        # Дожидаемся кликабельности и кликаем
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button)
        )
        register_button.click()
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))
        
        errors_messages = self._wait_for_elements(driver, AuthRegistre.ar_error_message, timeout=2)
        
        assert len(errors_messages) == 0 and driver.current_url == Urls.url_register
       
    # При некорректном email появляется ошибка
    @pytest.mark.parametrize('email', [
        'test1@yandexru', 
        'test2yandex.ru', 
        'te st3@yandex.ru', 
        'test4@ya ndex.ru', 
        '@yandex.ru', 
        'test6@.ru', 
        'test7@yandex.'
    ])
    def test_registration_incorrect_email_show_error(self, driver, email):
        driver.get(Urls.url_register)
        
        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Глотова Наталья')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(email)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('1478963qaz')
        
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button)
        )
        register_button.click()
        
        error_elements = self._wait_for_elements(driver, AuthRegistre.ar_error_message_2)
        
        assert len(error_elements) > 0 and error_elements[0].is_displayed()

    # При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'
    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password):
        driver.get(Urls.url_register)
        
        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Глотова Наталья')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('GlotovaNatalya55@yandex.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password)
        
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button)
        )
        register_button.click()
        
        error_elements = self._wait_for_elements(driver, AuthRegistre.ar_error_message)
        
        assert len(error_elements) > 0 and error_elements[0].is_displayed()
