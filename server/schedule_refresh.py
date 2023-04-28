"""
Отложенный старт для обновления данных
"""
import schedule, time, configJson, cacheData

def runup():
    preference = configJson.configScheduler()
    schedule.every(int(preference.schedule_period_query_value)).hours.do(cacheData.request_data())
    while True:
        schedule.run_pending()
        time.sleep(1)