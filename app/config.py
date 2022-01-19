import random


# Application configuration
DEBUG = True    # default is True, you can change it in create_app
SECRET_KEY = str(random.randint(10000, 31337))

# Database configuration
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS = True
