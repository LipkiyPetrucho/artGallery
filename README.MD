## Art Gallery Django Проект

### Стек технологий:
 - ![Python](https://img.shields.io/badge/Python-3.12-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)
 - ![Django](https://img.shields.io/badge/Django-5.1-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)
 - ![Docker](https://img.shields.io/badge/Docker-v25.0.3-grey?style=plastic&logo=docker&logoColor=white&labelColor=2496ED)
 - ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=336791)
 - ![Nginx](https://img.shields.io/badge/Nginx-1.25-grey?style=plastic&logo=nginx&logoColor=white&labelColor=269539)

### Описание проекта
**Art Gallery** — это веб-приложение для управления и отображения коллекции картин художника. Проект разработан с использованием Django и Docker, обеспечивая удобное управление картинами, блогом и контактной формой. В административной панели можно легко изменять статусы картин, такие как "Доступно", "Продано" или "Зарезервировано".

***

### Функционал

#### Модели Django:
- **Painting**: Картина с полями название, дата создания, материал, размеры, изображение, описание, категория и статус.
- **Post**: Блог-посты с полями заголовок, содержимое, изображение, видео, статус и автор.

#### Административная панель:
- Управление картинами с возможностью изменения их статусов.
- Управление блог-постами с фильтрацией по статусу.
- Возможность добавления, редактирования и удаления записей.

#### Контактная форма:
- Пользователи могут отправлять сообщения художнику с прикреплением файлов.
- Валидация ввода и отправка сообщений на указанный email художника.

#### Галерея картин:
- Отображение доступных картин с фильтрацией по статусу.
- Детальная страница для каждой картины с описанием и изображением.

#### Блог:
- Просмотр опубликованных постов.
- Детальная страница для каждого поста с возможностью просмотра других постов.

***

### API Endpoints
- #### GET /artworks/gallery/:
  Отображает галерею всех картин.
- #### GET /artworks/free-works/:
  Отображает только доступные для покупки картины.
- #### GET /artworks/painting/<id>/:
  Детальная страница конкретной картины.
- #### GET /blog/:
  Список опубликованных блог-постов.
- #### GET /blog/year/month/day/slug/:
  Детальная страница конкретного поста.
- #### GET/POST /artworks/contacts/:
  Форма для отправки сообщений художнику.

***

### Установка и запуск

#### Необходимые условия
Убедитесь, что в вашей системе установлено следующее:
- Docker
- Docker Compose
- Python 3.12+
- Аккаунт для электронной почты (например, Yandex) для настройки отправки писем

### Локальный запуск с Docker

<details>
<summary>Для запуска через Docker необходимо:</summary>

1. **Клонируйте репозиторий и перейдите в каталог проекта:**
    ```bash
    git clone https://github.com/yourusername/art_gallery.git
    cd art_gallery
    ```

2. **Пропишите переменные окружения в файле `.env`.**
    Создайте файл `.env` на основе `.env.example` и заполните необходимые значения:
    ```dotenv
    SECRET_KEY='Ваш_секретный_ключ_Django'
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

    # Настройки базы данных
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432

    # Настройки электронной почты
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.yandex.ru
    EMAIL_PORT=465
    EMAIL_USE_SSL=True
    EMAIL_USE_TLS=False
    EMAIL_HOST_USER=your_email@yandex.ru
    EMAIL_HOST_PASSWORD=your_email_password
    DEFAULT_FROM_EMAIL=your_email@yandex.ru
    ADMINS=Your Name:your_email@yandex.ru
    
    # Email художника для получения сообщений
    ARTIST_EMAIL=artist_email@yandex.ru
    ```

3. **Соберите и запустите контейнеры Docker:**
    ```bash
    docker-compose up --build
    ```

4. **Примените миграции базы данных:**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. **Создайте суперпользователя для доступа к административной панели:**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
    - Введите логин, например `admin`
    - Введите email (опционально)
    - Введите пароль

6. **Соберите статические файлы:**
    ```bash
    docker-compose exec web python manage.py collectstatic --noinput
    ```

</details>

***

### Доступ администратора
После выполнения шагов выше, вы можете получить доступ к административной панели Django:

- **Административная панель Django:** [http://localhost/admin/](http://localhost/admin/)
  - **Логин:** ваш созданный суперпользователь
  - **Пароль:** ваш пароль

***

### Запуск приложения
Как только контейнеры будут запущены, вы сможете получить доступ к приложению:
- **Главная страница:** [http://localhost:8000/](http://localhost:8000/)
- **Галерея:** [http://localhost:8000/artworks/gallery/](http://localhost:8000/artworks/gallery/)
- **Свободные работы:** [http://localhost:8000/artworks/free-works/](http://localhost:8000/artworks/free-works/)
- **Блог:** [http://localhost:8000/blog/](http://localhost:8000/blog/)
- **Контакты:** [http://localhost:8000/artworks/contacts/](http://localhost:8000/artworks/contacts/)

***

### Docker Setup
Проект включает в себя `Dockerfile` и `docker-compose.yml` для контейнерного развертывания:
- **Веб-контейнер (`web`)**: Запускает приложение Django.
- **База данных (`db`)**: Использует PostgreSQL.
- **Nginx (`nginx`)**: Обслуживает статические и медиа-файлы, проксирует запросы к Django.

### Лицензия
Проект распространяется по лицензии MIT. Подробнее см. файл [LICENSE](LICENSE).

***

<details>
<summary><b>Connect with me:</b></summary>
   <p align="left">
       <a href="mailto:pafos.light@gmail.com"><img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
       <a href="https://t.me/petr_lip"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
   </p>
</details>
