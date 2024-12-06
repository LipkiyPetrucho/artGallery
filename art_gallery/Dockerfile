FROM python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

## Установка WhiteNoise для обслуживания статических файлов в продакшн
#RUN pip install whitenoise
#
## Обновление настроек WSGI для WhiteNoise
#RUN sed -i "/application = get_wsgi_application()/a \
#from whitenoise import WhiteNoise\n\
#application = WhiteNoise(application, root='/app/static')" art_gallery/wsgi.py

EXPOSE 8000

CMD ["gunicorn", "art_gallery.wsgi:application", "--bind", "0.0.0.0:8000"]