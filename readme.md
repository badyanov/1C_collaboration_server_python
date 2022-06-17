# Аналог 1С:Система взаимодействия на Python

(На основе курса Низамова Ильи https://nizamov.school/)

## Установка виртуального окружения

`pip install virtualenv`

`python -m venv venv`

`.\venv\Scripts\activate.bat`

    Примечание:

    При попытке активировать виртуальное окружение может возникать ошибка безопасности PSSecurityException. Отключить эту проверку можно командой PowerShell (с правами администратора)

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

`pip install -r requirements.txt`

## Подготовка базы данных

Переходим в каталог django-проекта: **srv** и выполняем миграцию базы данных 

`cd srv`

`python manage.py migrate`

После этого создаем пользователя администратора и пароль

`python manage.py createsuperuser`

## Запуск приложения

`python manage.py runserver`

В админку можно попасть по адресу 
http://127.0.0.1:8000/admin/


## Сервисы:

* echo: ws://127.0.0.1:8000/ws/echo/
* collaboration: ws://127.0.0.1:8000/ws/cs/

