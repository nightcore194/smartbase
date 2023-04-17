"""
Запись данных в бд
"""
import databaseModel
def data_write(time, data):
    # отправка запроса к ранее подлюченной БД
    dataModel = databaseModel.Data(time_of_write=time, data_text=data)
    dataModel.save()