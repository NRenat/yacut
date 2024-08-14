# YACUT
Сервис для сокращения ссылок.

## Возможности
* Веб интерфейс для пользователей
* API доступ для разработчиков
* Генерация рандомных ссылок или своих

Документация к API хранится в [openapi.yml](openapi.yml).

# Запуск

* Установить зависимости 
```bash
pip install -r requirements.txt
```

* Шаблон переменных окружения можно найти тут: [жмяк](.env.example)

* Инициализировать БД

```bash
flask db init
```

* Применить миграции 

```bash
flask db migrate -m "Initial migration"
flask db upgrade
```
* Запуск приложения
```bash
flask run 
```

## Технологии
* Python 3.9
* Flask
* SQLAlchemy
* SQLite
* Flask-WTF
* WTForms
