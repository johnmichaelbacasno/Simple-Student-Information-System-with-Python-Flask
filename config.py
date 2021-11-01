from os import environ

class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY')

    MYSQL_DATABASE_HOST = environ.get('MYSQL_DATABASE_HOST')
    MYSQL_DATABASE_USER = environ.get('MYSQL_DATABASE_USER')
    MYSQL_DATABASE_PASSWORD = environ.get('MYSQL_DATABASE_PASSWORD')
    MYSQL_DATABASE_DB = environ.get('MYSQL_DATABASE_DB')

    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_BOOTSWATCH_THEME = None

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass