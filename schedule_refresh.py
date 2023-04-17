"""
Отложенный старт для обновления данных
"""
import json, schedule, cacheData, time

with open('settings.json', 'r') as file:
    preference = json.load(file)

def runup():
    schedule.every(int(preference['time'])).seconds.do(cacheData.request_data())
    while True:
        schedule.run_pending()
        time.sleep(1)