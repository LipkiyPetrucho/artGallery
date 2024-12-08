from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")


# Настройки безопасности
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 год
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CORS_ALLOW_CREDENTIALS = True

# CORS настройки
CORS_ALLOWED_ORIGINS = [
    "https://art-lipatova.ru",
    "https://www.art-lipatova.ru",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


# Добавление WhiteNoise для обслуживания статических файлов
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
] + MIDDLEWARE

# Настройки логирования для продакшн
LOGGING["handlers"]["file"]["level"] = "INFO"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["artworks"]["level"] = "INFO"
