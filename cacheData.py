"""
Получение данных с api в формате json
"""
import configJson, requests
from dataHandler import data_handler

def request_data():
    preference = configJson.getData()
    data = requests.get(url=preference['url'], headers=preference['url'], params=preference['params']).json()
    data_handler(data)
    return data



