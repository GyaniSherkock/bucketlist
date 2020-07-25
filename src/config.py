import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:gyanish4150@localhost:5432/bucket_list"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "postgres://postgres:ashish4150@database-1.cxt5wurz5hfp.us-east-2.rds.amazonaws.com:5432/shopping_centre_db"

# For testing the testcases locally. Don't delete it.
class Testing(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


# Below is for the setting up of app using the Environmental variable.
app_config = {
    'development' : Development,
    'production' : Production,
    'testing' : Testing,
    'FLASK_ENV' : os.getenv('FLASK_ENV')
    # In the Flask Env we use 'developement or production'. It refers to here which calls the Development and Prouction class
}



