import datetime
from api.models import db
from os import getenv

SECRET_KEY = getenv('OSL_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL').replace('postgres', 'postgresql')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY = db
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7)
#REMEMBER_COOKIE_DURATION=datetime.timedelta(days=7)
SESSION_COOKIE_SECURE=False
REMEMBER_COOKIE_HTTPONLY=True
STATIC_FOLDER = 'static'
SESSION_COOKIE_SAMESITE = 'None'
