#!/usr/bin/env bash

# test/prod
if [ "$VEAT_DB_SERVICE_HOST" ]; then
    host=$VEAT_DB_SERVICE_HOST
    echo "Setting host to VEAT_DB_SERVICE_HOST"

else
    host="db"
    echo "Setting host to 'db'"
fi

# add credentials to a .pgpass file
echo $host:"*:*:postgres:$POSTGRES_PASSWORD" | tee ~/.pgpass > /dev/null 2>&1
#
chmod 0600 ~/.pgpass

until psql -h "$host" -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 10
done

echo "Beginning database migration"
python manage.py migrate --noinput

echo "Collecting static files"
python manage.py collectstatic --noinput -v 0

echo "Creating admin user"
python -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('default').create_superuser( \
   username='$DJANGO_SU_NAME', \
   email='$DJANGO_SU_EMAIL', \
   password='$DJANGO_SU_PASSWORD')"

echo "Installing fixtures"
python manage.py loaddata energy_audit/fixtures/*.json


>&2 echo "Postgres is up - executing command"

        echo "Starting Gunicorn."
        exec gunicorn web.wsgi:application \
             --name web \
             --bind 0.0.0.0:8000 \
             --workers 3 \
             --log-level=debug \
             --env DJANGO_SETTINGS_MODULE=web.settings \


