## Тестовое задание для Craft Group

## Установка:
1. Создаем новое виртуальное окружение и клонируем туда наш проект.

```shell
python3.8 -m venv assignment
cd assignment
. bin/activate
mkdir src && cd src
git clone https://github.com/Boring-Mind/rest-assignment2 .
```

> Если в системе нет python версии 3.8, то устанавливаем его по [инструкции](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu).

2. Устанавливаем зависимости

```shell
pip install -U pip
pip install -r requirements.txt
```

3. Инициализируем базу данных и запускаем проект

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. Тестируем проект

* Заходим по адресу 127.0.0.1:8000
* Перед входом в систему нужно зарегистирировать нового пользователя.
* Чтобы сортировать список пользователей через API, нужно добавить к URL GET-параметр ordering. К примеру, http://127.0.0.1:8000/api/list_users/?ordering=-username - сортировка имен пользователей по убыванию. Можно сортировать по нескольким полям: ?ordering=-username,email - сортировка по именам пользователей по убыванию и по адресам электронной почты.
* Все остальные функции есть в шапке сайта.
