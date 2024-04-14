# YACUT - сервис сокращения ссылок

Пользователи могут воспользоваться веб версией или использовать API. 

Документация к API хранится в [openapi.yml](openapi.yml).

# Запуск

* Установить зависимости 
```bash
pip install -r requirements.txt
```

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
