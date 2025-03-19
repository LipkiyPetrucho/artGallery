from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["art-lipatova.ru", "www.art-lipatova.ru"]

# Настройки логирования для разработки
LOGGING["handlers"]["file"]["level"] = "DEBUG"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["artworks"]["level"] = "DEBUG"
