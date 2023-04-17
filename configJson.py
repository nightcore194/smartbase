"""
Получение данных из файла настроек в формате JSON
"""
import json
def getData():
    with open('settings.json', 'r') as file:
        preference = json.load(file)
    return preference