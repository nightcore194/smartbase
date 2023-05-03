"""
Отложенный старт для обновления данных
"""
import schedule, time, server.configJson, server.cacheData

def runup():
    preference = server.configJson.configScheduler()
    schedule.every(int(preference.schedule_period_query_value)).hours.do(server.cacheData.request_data()) # отложенный старт с периодичностью в n часов
    while True:
        schedule.run_pending()
        time.sleep(1)