"""
Подготовка базы данных
"""
import server.configJson, peewee
from playhouse.migrate import *
from flask_sqlalchemy import SQLAlchemy
from app import app

def setup_connection():
    try:
        # подключение к базе данных
        preference = server.configJson.configDB()
        db = SQLAlchemy(app)
        return db
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)