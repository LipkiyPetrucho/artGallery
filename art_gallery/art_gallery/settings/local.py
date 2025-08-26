from .settings import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "art-lipatova.ru",
    "www.art-lipatova.ru",
    ".ngrok-free.app",  # Разрешает все поддомены ngrok
    "3e15-192-119-10-202.ngrok-free.app",  # Конкретный домен
]

# Локальная БД для разработки
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Настройки логирования для разработки
LOGGING["handlers"]["file"]["level"] = "DEBUG"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["artworks"]["level"] = "DEBUG"

CSRF_TRUSTED_ORIGINS = [
    "https://art-lipatova.ru",
    "https://www.art-lipatova.ru",
    "https://*.ngrok-free.app",
    "https://3e15-192-119-10-202.ngrok-free.app"
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True

