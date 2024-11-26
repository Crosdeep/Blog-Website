import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # PostgreSQL veritabanı bağlantı URI'si
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:pp123@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('pinarpinar959@gmail.com')
    MAIL_PASSWORD = os.environ.get('')
    MAIL_DEFAULT_SENDER = os.environ.get('como.pinar1631@gmail.com') or 'como.pinar1631@gmail.com'


