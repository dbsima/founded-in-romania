import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # Secret key for the app
    SECRET_KEY = os.environ['SECRET_KEY']
    # Database URI that is written in venv/bin/activate
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # Credentials to access typeform API (https://admin.typeform.com/account)
    TYPEFORM_FORM_UID = os.environ['TYPEFORM_FORM_UID']
    TYPEFORM_API_KEY = os.environ['TYPEFORM_API_KEY']
    # Credentials for admin
    ADMIN_USER = 'admin'
    ADMIN_PASS = 'password'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
