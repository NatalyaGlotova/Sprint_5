class Urls:

    # Базовый адрес сервера (вынесла в отдельную переменную)
    BASE_URL = 'https://stellarburgers.education-services.ru/'

    # Главная страница - Конструктор
    url_main_page = BASE_URL

    # Ссылка на страницу авторизации (Личный кабинет)
    url_login = f'{BASE_URL}login'

    # Ссылка на страницу Профиль 
    url_profile = f'{BASE_URL}account/profile'

    # Ссылка на страницу регистрации
    url_register = f'{BASE_URL}register'

    # Ссылка на страницу восстановления пароля
    url_forgot_password = f'{BASE_URL}forgot-password'
    