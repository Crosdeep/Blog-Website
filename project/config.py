#project/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pp123@localhost/blog'

    try:
        SQLALCHEMY_DATABASE_URI ='postgresql://postgres:pp123@localhost:5432/blog'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    except KeyError as e:
        print(e)




