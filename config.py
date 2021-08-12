import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=b1c90d00a6e14923aed224401a3aaa61'
    SEARCH_API_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-08-12&sortBy=popularity&apiKey=API_KEY'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
