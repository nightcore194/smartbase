"""
Модель представления БД
"""
import server.databaseSetup, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, DateTime, Text, String
# реализация струткуры ORM
# соединение с базой
db = server.databaseSetup.setup_connection()
Base = declarative_base()

# Определяем модель данных(в качестве примера взял базу данных, которую описал в коде ранее)
class Data(Base):
    __tablename__ = 'data'
    id_data = Column(Integer, primary_key=True, autoincrement=True)
    time_of_data = Column(DateTime)
    data_text = Column(Text,  unique=True)
    def __init__(self, id_data, data_text):
        self.id_data = id_data
        self.time_of_data = time.strftime('%Y-%m-%d %H:%M:%S', 'utc')
        self.data_text = data_text

    def __repr__(self):
        return f"<{self.id_data}:{self.time_of_data}:{self.data_text}>"

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True)
    password = Column(String(64),  unique=True)
    def __init__(self, id_user, username, password):
        self.id_user = id_user
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<{self.id_user}:{self.username}>"

class Predict(Base):
    __tablename__ = 'predict'
    id_predict = Column(Integer, primary_key=True, autoincrement=True)
    no_vk = Column(Integer, unique=True)
    no_siom = Column(Integer, unique=True)
    match_predict = Column(Integer)
    def __init__(self, id_predict, no_vk, no_siom, match_predict):
        self.id_predict = id_predict
        self.no_vk = no_vk
        self.no_siom = no_siom
        self.match_predict = match_predict

    def __repr__(self):
        return f"<{self.id_predict}:{self.no_vk}:{self.no_siom}:{self.match_predict}>"

class Used(Base):
    __tablename__ = 'used'
    id_used = Column(Integer, primary_key=True, autoincrement=True)
    no_vk = Column(Integer, unique=True)
    no_siom = Column(Integer, unique=True)
    match_predict = Column(Integer)
    date_of_usage = Column(DateTime)
    def __init__(self, id_predict, no_vk, no_siom, match_predict):
        self.id_predict = id_predict
        self.no_vk = no_vk
        self.no_siom = no_siom
        self.match_predict = match_predict
        self.date_of_usage = time.strftime('%Y-%m-%d %H:%M:%S', 'utc')

    def __repr__(self):
        return f"<{self.id_predict}:{self.no_vk}:{self.no_siom}:{self.match_predict}>"

Base.metadata.create_all(db.engine)