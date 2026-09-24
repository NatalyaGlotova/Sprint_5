import random

class PersonData:
    user_name = 'Глотова Наталья'
    login  = 'GlotovaNatalya55@yandex.ru'
    password = '1478963qaz'

class ValidData:
    #user_name = 'Тестов Тест'
    @property
    def user_name(self) -> str:
        """Возвращает случайное имя в формате Тест_XX"""
        return f"Тест_{random.randint(1000, 9999)}"

    @property
    def login(self):
        return f'Test{random.randint(1000, 9999)}@yandex.ru'

    @property
    def password(self):
        return f'{random.randint(100000, 999999)}'
data = ValidData()