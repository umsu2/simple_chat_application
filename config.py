class Config:
    """
    Common configs
    """

class DevelopmentConfig(Config):
    """
    Dev Config
    """


    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False


