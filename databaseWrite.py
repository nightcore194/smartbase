"""
Запись данных в бд
"""
import datetime, databaseModel
def data_write(data):
    # отправка запроса к ранее подлюченной БД
    dataModel = databaseModel.Data(time_of_write=datetime.datetime.now(), data_text=data)
    dataModel.save()