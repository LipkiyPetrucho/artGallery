#!/bin/bash
set -e

echo "Waiting for database..."
# Ждем пока база данных будет готова
until python manage.py check --database default 2>/dev/null; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

echo "Database is up - executing migrations"
python manage.py migrate --noinput

echo "Starting server"
exec "$@"
