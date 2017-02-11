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

config_mapping = {
    'dev' : DevelopmentConfig,
    'prod' : ProductionConfig,
}
def get_config(name):
    if name in config_mapping:
        return config_mapping[name]
    raise NameError('{} is not a valid config'.format(name))
