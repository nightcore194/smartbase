"""
Запись данных в бд
"""
import time, server.models
def data_write(data):
    # отправка запроса к ранее подлюченной БД
    dataModel = server.models.Data(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S', 'utc'), data_text=data)
    dataModel.save()

def predict_write(predict):
    # отправка запроса к ранее подлюченной БД
    predictModel = server.models.Predict(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S', 'utc'), predict_data_text=predict)
    predictModel.save()