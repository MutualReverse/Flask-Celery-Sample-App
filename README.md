# Flask-Celery-Sample-App
Simple example Flask app using Celery as worker

## Install
```pip install -r requirements.txt```

## Requirements
- Redis link (paste the redis url and port in .env file)
- Copy .env.example to .env
## Run Application
```gunicorn --reload --bind=0.0.0.0 app:app```

and in separate window

```celery -A app.celery_app worker --loglevel INFO```
