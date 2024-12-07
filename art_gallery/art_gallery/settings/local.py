from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "www.art-lipatova.ru", "art-lipatova.ru"]

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATICFILES_DIRS = [BASE_DIR / "static"]

# Настройки логирования для разработки
LOGGING["handlers"]["file"]["level"] = "DEBUG"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["artworks"]["level"] = "DEBUG"
