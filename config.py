import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maranatha:marahuwase@localhost/oneminutepitch'


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maranatha:marah31998@localhost/oneminutepitch_test'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maranatha:marah31998@localhost/oneminutepitch'
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}