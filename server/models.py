"""
Модель представления БД
"""
import server.databaseSetup
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, DateTime, Text, String
# реализация струткуры ORM
# соединение с базой
db = server.databaseSetup.setup_connection()
Base = declarative_base()

# Определяем модель данных(в качестве примера взял базу данных, которую описал в коде ранее)
class Data(Base):
    __tablename__ = 'data'
    id_data = Column(Integer, primary_key=True)
    time_of_data = Column(DateTime, unique=True)
    data_text = Column(Text,  unique=True)
    def __init__(self, id_data, time_of_data, data_text):
        self.id_data = id_data
        self.time_of_data = time_of_data
        self.data_text = data_text

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id_data, self.time_of_data, self.data_text)

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    password = Column(String(64),  unique=True)
    def __init__(self, id_user, username, password):
        self.id_user = id_user
        self.username = username
        self.password = password

    def __repr__(self):
        return "<{}:{}>".format(self.id_user, self.username)

class Predict(Base):
    __tablename__ = 'predict'
    id_predict = Column(Integer, primary_key=True)
    time_of_predict = Column(DateTime, unique=True)
    predict_text = Column(Text, unique=True)
    def __init__(self, id_predict, time_of_predict, predict_text):
        self.id_predict = id_predict
        self.time_of_predict = time_of_predict
        self.predict_text = predict_text

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id_predict, self.time_of_predict, self.predict_text)

Base.metadata.create_all(db.engine)