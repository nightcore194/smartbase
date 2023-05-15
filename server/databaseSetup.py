"""
Подготовка базы данных
"""
import server.configJson, peewee
from playhouse.migrate import *
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
def setup_connection():
    try:
        # подключение к базе данных
        preference = server.configJson.configDB()
        current_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2:///{preference.user_value}:{preference.password_value}@{preference.host_value}/{preference.db_name_value}"
        db = SQLAlchemy(current_app)
        return db
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)