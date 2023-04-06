# """Flask configuration."""
import os


class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = "6c35237bb89c22463451387a0aec5d78"
    CELERY = {        
        "broker_url": os.getenv("REDIS_URL"),
        "result_backend": os.getenv("REDIS_URL"),
        "broker_transport_options": {
            'visibility_timeout': 120,
            'queue_name_prefix': 'celery-',
            'timezone': 'America/Los_Angeles'
        }
    }
    


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///test-data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
