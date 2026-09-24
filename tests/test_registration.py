import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AuthRegistre, AuthLogin

from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:

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
        
        # Ждем перехода на страницу логина.
        # Проверяем появление элемента с текстом "Вход"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLogin.al_element_with_login_text)
        )

        assert driver.current_url == Urls.url_login 

    # При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет
    def test_registration_empty_name_nothing_happens(self, driver):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_email_field).send_keys('GlotovaNatalya55@yandex.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('1478963qaz')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))
    
        errors_messages = driver.find_elements(*AuthRegistre.ar_error_message)

        assert driver.current_url == Urls.url_register and len(errors_messages) == 0


    # При некорректном email появляется ошибка, что пользователь уже существует 
    @pytest.mark.parametrize('email_list', ['test1@yandexru', 'test2yandex.ru', 'te st3@yandex.ru', 'test4@ya ndex.ru',
                                            '@yandex.ru', 'test6@.ru', 'test7@yandex.'])
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Глотова Наталья')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(email_list)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('1478963qaz')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthRegistre.ar_error_message_2))
        error_message = driver.find_element(*AuthRegistre.ar_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'


    # При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'
    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Глотова Наталья')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('GlotovaNatalya55@yandex.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthRegistre.ar_error_message))
        error_message = driver.find_element(*AuthRegistre.ar_error_message)

        assert error_message.text == 'Некорректный пароль'
