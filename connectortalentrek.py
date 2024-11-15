import os

# Database configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/app_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for app
SECRET_KEY = os.urandom(24)
