web: python manage.py collectstatic
web: daphne whatsappclone1.asgi.application -- port $PORT --bind 0.0.0.0 -v2
chatwalker: python manage.py runwalker --settings=chat.settings -v2