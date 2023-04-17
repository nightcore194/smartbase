"""
Получение данных с api в формате json и запись в БД
"""
import json, requests, sqlite3, setupDataBase, datetime

with open('settings.json', 'r') as file:
    preference = json.load(file)

def request_data():
    data = requests.get(url=preference['url'], headers=preference['url'], params=preference['params']).json()
    data_handler(data)
    return data

def data_handler(data):
    # here past your data handler method and erase pass
    data_write(data, datetime.datetime.now())

def data_write(data, time):
    setupDataBase.setup()
    conn = sqlite3.connect('cacheData.db')
    c = conn.cursor()
    c.execute(f'''
              INSERT INTO data values({time}{data})
              ''')
    conn.commit()
    conn.close()