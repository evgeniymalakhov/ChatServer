if [ $AUTO_MIGRATE == True ]; then
  echo "=> Performing database migrations..."
  python ChatServer/manage.py migrate
fi