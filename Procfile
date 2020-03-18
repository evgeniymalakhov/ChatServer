web: daphne ChatServer.asgi:application --port $PORT --bind 0.0.0.0 -v2
serverworker: python manage.py runworker --settings=ChatServer.settings -v2
release: python manage.py migrate