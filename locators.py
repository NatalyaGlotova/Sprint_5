from selenium.webdriver.common.by import By

# Главная страница
class MainPage:
    # кнопка "Конструктор"
    mn_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")   
    # Логотип "Stellar Burgers"                                     
    mn_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    # Кнопка "Личный кабинет"
    mn_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    # Кнопка "Войти в аккаунт"
    mn_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Кнопка "Оформить заказ"
    mn_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Заголовок конструктора "Соберите бургер"
    mn_constructor_header = (By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")

    # Разделы
    # Кнопка "Булки"
    mn_bun_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    # Раздел «Булки»
    mn_h_bun = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
    # Кнопка "Соусы"
    mn_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    # Раздел "Соусы"
    mn_h_sauces = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    # Кнопка "Начинки"
    mn_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    # Раздел "Начинки"
    mn_h_filling = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")

# Страница авторизации (Личный кабинет)
class AuthLogin:
    # Заголовок формы авторизации
    al_login_text = (By.XPATH, ".//h2[text()='Вход']")
    # кнопка "Войти"
    al_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")
    # кнопка "Войти" с ссылкой
    al_login_text_with_href = (By.XPATH, ".//a[text()='Войти']") 
    # Кнопка "Зарегистророваться" и "Восстановить пароль"
    al_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
    # Поле ввода email
    al_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    # Поле ввода пароля
    al_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    al_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")

# Страница регистрации
class AuthRegistre:
    # Плейсхолдер "Имя"
    ar_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    # Плейсхолдер "email"
    ar_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    # Плейсхолдер "Пароль"
    ar_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    # Кнопка  "Зарегистрироваться"
    ar_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Ошибка - такой пользователь уже существует
    ar_error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    # Ошибка - Некорректный логин или пароль
    ar_error_message_2 = (By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")
    # уже зарегистрированы? Кнопка "Войти"
    ar_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")

# Страница восстановления пароля
class AuthPassword:
    # Кнопка со ссылкой "Войти"
    ap_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")

# страница Профиль
class LKProfile:
    # Кнопка "Выход"
    lk_logout_button = (By.XPATH, ".//button[text()='Выход']")
    # Персональные данные
    lk_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    # Кнопка "История покупок"
    lk_history_shop_button = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

