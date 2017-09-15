import os


class Config(object):
    """
    Common configurations
    """

    if 'RDS_HOSTNAME' in os.environ:
        DATABASES = {
            'default': {
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}