from dotenv import load_dotenv
load_dotenv()                 

import os

db_ip = os.environ.get('DB_IP')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mariadb+mariadbconnector://{db_user}:{db_pass}@{db_ip}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mariadb+mariadbconnector://{db_user}:{db_pass}@{db_ip}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}