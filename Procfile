release: python manage.py migrate
web: gunicorn -b :$PORT ChatServer.wsgi