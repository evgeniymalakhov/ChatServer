if [ $AUTO_MIGRATE == True ]; then
  echo "=> Performing database migrations..."
  python 'app_name'/manage.py migrate
fi