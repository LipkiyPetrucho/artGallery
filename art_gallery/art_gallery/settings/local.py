from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

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
