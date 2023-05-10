## Проект yamdb_final

![yamdb_workflow](https://github.com/DanMalikov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание.
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Технологии

- Python 3.7

- Django 2.2.19

- Nginx

- Docker-compose

## Установка

Для запуска приложения проделайте следующие шаги:

1. Склонируйте репозиторий.
2. Перейдити в папку infra и запустите docker-compose.yaml (при установленном и запущенном Docker)
```
docker-compose up
```
3. Для пересборки контейнеров выполните команду:
```
docker-compose up -d --build
```
4. В контейнере web выполните миграции:
```
docker-compose exec web python manage.py migrate
```
5. Создатйте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
6. Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Проект запущен и доступен по адресу: [localhost](http://localhost/admin/)

### Автор
- Данила Маликов
