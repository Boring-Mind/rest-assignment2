# rest-assignment2
Test assignment of the Craft Group

## Установка:
1. Создаем новое виртуальное окружение и клонируем туда наш проект.

* python3 -m venv assignment
* cd assignment
* . bin/activate
* mkdir src && cd src
* git clone https://github.com/Boring-Mind/rest-assignment2 .

2. Устанавливаем зависимости

* pip install -U pip
* pip install -r requirements.txt

3. Инициализируем базу данных и запускаем проект

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

4. Тестируем проект

* Заходим по адресу 127.0.0.1:8000
* Перед входом в систему нужно зарегистирировать нового пользователя.
* Все остальные функции есть в шапке сайта.
