from celery import Celery
from celery import Task
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app(testing=False, **kwargs):
    """Create Flask application"""
    app = Flask(__name__, **kwargs)
    app_mode = "testing" if testing else os.getenv("FLASK_ENV", "production")

    if app_mode is not None:
        if app_mode == "testing":
            app.config.from_object("config.TestingConfig")
        elif app_mode == "development":
            app.config.from_object("config.DevelopmentConfig")
        elif app_mode == "production":
            app.config.from_object("config.ProductionConfig")
        else:
            raise RuntimeError("Unknown environment setting provided.")

    celery_init_app(app)
    
    @app.route("/")
    def index() -> str:
        return 'Hello World'
    
    from . import views
    app.register_blueprint(views.bp)

    return app


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app