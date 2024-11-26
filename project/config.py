import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'cokgizlicok'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:pp123@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



