# Работа в рамках обучения на курсе по автоматизации тестирования на Pytest+Selenium WebDriver

## Обращение к рецензентам:
Пожалуйста, прочтите README перед проверкой теста

1. Виртуальное окружение
Виртуальное окружение в проекте задано с помощью poetry. Установка poetry описана [здесь](https://python-poetry.org/docs/)

Клонируйте репозиторий
```
git clone git@github.com:mark-rom/pytest_selenium_stepik_course.git
```
Перейдите в папку проекта
```
cd pytest_selenium
```
Установите зависимости
```
poerty install
```

2. Тест лежит в папке tests
Команда для запуска внутри виртуального окружения
```
pytest --language=es
```
либо без виртуального окружения, но с установленными зависимостями poetry
```
poetry run pytest --language=es
```