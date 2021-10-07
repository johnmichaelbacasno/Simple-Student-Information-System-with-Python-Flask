class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = '1234'

    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'localhost1234'
    MYSQL_DATABASE_DB = 'ssis'

    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_BOOTSWATCH_THEME = None

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass