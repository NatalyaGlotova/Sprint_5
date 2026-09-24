from locators import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersConstructorForm:

    # Проверка перехода на "Соусы"
    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        
        # Нажимаем на вкладку "Соусы"
        driver.find_element(*MainPage.mn_sauces_button).click()

        active_sauces_xpath = f"{MainPage.mn_sauces_button[1]}[contains(@class, 'tab_tab_type_current')]"
        
        # Вся проверка и ожидание маркера успеха 
        assert WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, active_sauces_xpath).is_displayed()
        ), "Вкладка 'Соусы' не стала активной после клика"

    # Проверка перехода на "Начинки"
    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        
        # Нажимаем на вкладку "Начинки"
        driver.find_element(*MainPage.mn_filling_button).click()

        active_filling_xpath = f"{MainPage.mn_filling_button[1]}[contains(@class, 'tab_tab_type_current')]"
        
        # Вся проверка и ожидание маркера успеха
        assert WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, active_filling_xpath).is_displayed()
        ), "Вкладка 'Начинки' не стала активной после клика"

    # Проверка перехода на "Булки"
    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        
        # Сначала уходим на "Соусы", чтобы вкладка "Булки" перестала быть активной
        driver.find_element(*MainPage.mn_sauces_button).click()
        
        # Возвращаемся на "Булки"
        driver.find_element(*MainPage.mn_bun_button).click()
        active_bun_xpath = f"{MainPage.mn_bun_button[1]}[contains(@class, 'tab_tab_type_current')]"
        
        # Ожидание активации и проверка маркера успеха
        assert WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, active_bun_xpath).is_displayed()
        ), "Вкладка 'Булки' не стала активной после клика"
        
