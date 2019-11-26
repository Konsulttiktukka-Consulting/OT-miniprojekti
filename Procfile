release: export FLASK_APP=application && flask init-db
web: gunicorn --preload --workers 1 application:app
