"""
Модель представления БД
"""
import server.databaseSetup, peewee
# реализация струткуры ORM
# соединение с базой

db = server.databaseSetup.setup_connection()

# Определяем модель данных(в качестве примера взял базу данных, которую описал в коде ранее)
class Data(db.Model):
    id_data = db.Column(db.Integer, primary_key=True)
    time_of_data = db.Column(db.DateTime, unique=True)
    data_text = db.Column(db.Text,  unique=True)
    def __init__(self, id_data, time_of_data, data_text):
        self.id_data = id_data
        self.time_of_data = time_of_data
        self.data_text = data_text

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id_data, self.time_of_data, self.data_text)

class Predict(db.Model):
    id_predict = db.Column(db.Integer, primary_key=True)
    time_of_predict = db.Column(db.DateTime, unique=True)
    predict_text = db.Column(db.Text, unique=True)
    def __init__(self, id_predict, time_of_predict, predict_text):
        self.id_predict = id_predict
        self.time_of_predict = time_of_predict
        self.predict_text = predict_text

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id_predict, self.time_of_predict, self.predict_text)