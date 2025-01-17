# Flower Delivery - итоговый проект "Программист на Python с нуля" от Zerocoder

## Описание проекта

**Razonova Final Project** — это система для доставки цветов, построенная с использованием Django. Она включает несколько приложений для управления заказами, 
пользователями, каталогом товаров и аналитикой. Пользователи могут просматривать товары, оформлять заказы и отслеживать статус своих заказов через Telegram-бота. 
Администраторы могут управлять заказами и просматривать отчеты о продажах и популярности товаров.

## Стек технологий

- **Django** — фреймворк для создания веб-приложений.
- **SQLite** — база данных.
- **Python** — язык программирования.
- **aiogram** — библиотека для создания Telegram-ботов.
- **Aiohttp** — для обработки HTTP-запросов в асинхронном режиме.
- **LocalTunnel** — для создания публичных URL для вебхуков.

## Структура проекта

Rozanova_final_project/
│
├── .venv/                        # Виртуальное окружение
├── .gitignore                    # Файл игнорирования для Git
├── LICENSE                       # Лицензия проекта
├── requirements.txt              # Зависимости проекта
├── df/                           # Основной каталог проекта
│   ├── __init__.py               # Инициализация пакета
│   ├── asgi.py                   # Настройки ASGI для проекта
│   ├── settings.py               # Настройки Django
│   ├── urls.py                   # Главные маршруты проекта
│   ├── wsgi.py                   # Точка входа для WSGI сервера
│   ├── analytics/                # Приложение для аналитики
│   │   ├── admin.py              # Административная панель
│   │   ├── models.py             # Модели для аналитики
│   │   ├── views.py              # Представления для аналитики
│   │   ├── tests.py              # Тесты для аналитики
│   │   └── migrations/           # Миграции для аналитики
│   ├── bot/                      # Приложение для Telegram-бота
│   │   ├── db_controller.py      # Контроллер базы данных для бота
│   │   ├── main.py               # Логика бота
│   ├── catalog/                  # Приложение для каталога товаров
│   │   ├── admin.py              # Административная панель для каталога
│   │   ├── models.py             # Модели товаров
│   │   ├── forms.py              # Формы для каталога
│   │   ├── views.py              # Представления для каталога
│   │   ├── tests.py              # Тесты для каталога
│   │   └── urls.py               # Маршруты для каталога
│   ├── img/                      # Папка с изображениями
│   │   ├── products/             # Изображения товаров
│   ├── main/                     # Основное приложение
│   │   ├── admin.py              # Административная панель для основного приложения
│   │   ├── forms.py              # Формы для основного приложения
│   │   ├── models.py             # Модели основного приложения
│   │   ├── views.py              # Представления для основного приложения
│   │   ├── tests.py              # Тесты для основного приложения
│   │   ├── migrations/           # Миграции для основного приложения
│   │   └── urls.py               # Маршруты для основного приложения
│   ├── orders/                   # Приложение для заказов
│   │   ├── admin.py              # Административная панель для заказов
│   │   ├── forms.py              # Формы для заказов
│   │   ├── models.py             # Модели заказов
│   │   ├── views.py              # Представления для заказов
│   │   ├── signals.py            # Сигналы для заказов
│   │   ├── tests.py              # Тесты для заказов
│   │   ├── urls.py               # Маршруты для заказов
│   │   ├── templates/            # Шаблоны для заказов
│   │   │   ├── analytics_report.html # Отчет по аналитике заказов
│   │   │   ├── checkout.html     # Шаблон оформления заказа
│   │   │   ├── order_list.html   # Список заказов
│   │   │   ├── order_success.html # Успешное оформление заказа
│   │   │   └── order_update.html  # Обновление статуса заказа
│   ├── users/                    # Приложение для пользователей
│   │   ├── admin.py              # Административная панель для пользователей
│   │   ├── forms.py              # Формы для пользователей
│   │   ├── models.py             # Модели пользователей
│   │   ├── Profile.py            # Профиль пользователя
│   │   ├── views.py              # Представления для пользователей
│   │   ├── tests.py              # Тесты для пользователей
│   │   ├── urls.py               # Маршруты для пользователей
│   │   └── migrations/           # Миграции для пользователей
└── CopyDB/                       # Папка для работы с копиями БД
    ├── db.sqlite3                # Копия базы данных
    ├── config.py                 # Конфигурация
    └── sing-box-config.json      # Конфигурационный файл для синхронизации

## Установка и настройка

### 1. Клонирование репозитория

Клонируйте репозиторий с проектом:

git clone <URL вашего репозитория>
cd Rozanova_final_project

2. Создание виртуального окружения
Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows

3. Установка зависимостей
Установите все зависимости:

pip install -r requirements.txt

4. Применение миграций
Примените миграции для создания базы данных:

python manage.py migrate
5. Запуск сервера

python manage.py runserver

Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/.

### Описание моделей
#### Модели пользователей (users/models.py)

User — модель пользователя с дополнительными полями: phone, address, telegram_id.
Profile — модель профиля пользователя с дополнительным полем telegram_id.

#### Модели заказов (orders/models.py)

Order — модель для хранения информации о заказе, включая статус, уникальный ключ и информацию о доставке.
OrderItem — модель для товаров в заказе с указанием количества.
OrderStatusHistory — история изменения статуса заказа.

#### Модели товаров (catalog/models.py)

Product — модель для хранения информации о товаре (например, название, цена).

### Основные функции

Регистрация и авторизация
/register — страница регистрации пользователя.
/login — страница входа пользователя.
/logout — выход из системы.

Заказы
/checkout — оформление заказа.
/order_success — страница успеха после оформления заказа с указанием уникального ключа.
/order_list — список заказов для администратора.
/order_update — обновление статуса заказа.

Telegram-бот
/start — приветствие и инструкции по использованию.
/status <unique_key> — получение статуса заказа по уникальному ключу.

Аналитика
/analytics_report — отчет о популярности товаров, доходах по статусам заказов, и количество заказов по дням.
/order_report — отчет по заказам с фильтрацией и пагинацией.
/export_analytics_csv — экспорт аналитики в CSV файл.

## Лицензия
Проект распространяется под лицензией MIT.
