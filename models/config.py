import os

class metrics_db_config(object):
    bind_name = "metrics" 
    SQLALCHEMY_DATABASE_URI = os.environ['SQL_URL']
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
