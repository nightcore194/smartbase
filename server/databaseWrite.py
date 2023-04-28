"""
Запись данных в бд
"""
import time, server.models
def data_write(data):
    # отправка запроса к ранее подлюченной БД
    dataModel = server.models.Data(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S'), data_text=data)
    dataModel.save()