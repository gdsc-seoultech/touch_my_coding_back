import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    load_dotenv()

    db = {
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PW"),
        "host": os.environ.get("DB_HOST"),
        "port": os.environ.get("DB_PORT"),
        "database": os.environ.get("DB_DATABASE"),
    }

    DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = (
        # os.environ.get("DEV_DATABASE_URL")
        # or DB_URL
        DB_URL
    )