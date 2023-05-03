"""
Запись данных в бд
"""
import time, server.models, server.databaseSetup

db = server.databaseSetup.setup_connection()
def data_write(data):
    # отправка запроса к ранее подлюченной БД
    dataModel = server.models.Data(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S', 'utc'), data_text=data)
    db.session.add(dataModel)
    db.session.commit()

def predict_write(predict):
    # отправка запроса к ранее подлюченной БД
    predictModel = server.models.Predict(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S', 'utc'), predict_data_text=predict)
    db.session.add(predictModel)
    db.session.commit()