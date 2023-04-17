"""
Обработка полученных данных в формате json
"""
import datetime, databaseWrite
def data_handler(data):
    # here past your data handler method and erase pass
    databaseWrite.data_write(datetime.datetime.now(), data)