# API Yatube

## Описание

API Yatube представляет собой интерфейс для взаимодействия с социальной платформой Yatube. Платформа предоставляет возможность публикации постов, комментирования, подписки на других пользователей и другие социальные функции.

## Установка

1. Клонируйте репозиторий `api_final_yatube` в вашу рабочую директорию.

    ```bash
    git clone https://github.com/your_username/api_final_yatube.git
    ```

2. Создайте и активируйте виртуальное окружение.

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/MacOS
    venv\Scripts\activate  # для Windows
    ```

3. Установите необходимые пакеты.

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции.

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер.

    ```bash
    python manage.py runserver
    ```

6. API будет доступно по адресу http://127.0.0.1:8000/redoc/.

## Примеры

### Примеры запросов к API:

- Получить все посты:

    ```bash
    GET /posts/
    ```

- Создать новый пост:

    ```bash
    POST /posts/
    {
        "text": "Новый пост"
    }
    ```

- Получить все комментарии к посту с id=1:

    ```bash
    GET /posts/1/comments/
    ```

## Системные требования

- Python 3.8 и выше
- Django 3.2 и выше
- Django REST framework 3.12 и выше

## Планы по доработке

- Реализовать модель Follow и соответствующие эндпоинты.
- Добавить возможность поиска постов по хэштегам.
- Расширить функционал комментариев.

## Стек технологий

- Python
- Django
- Django REST framework

## Коллекция запросов для Postman

В директории `postman_collection` сохранена коллекция запросов для отладки и проверки работы текущей версии API Yatube. Импортируйте коллекцию в Postman для выполнения запросов.
