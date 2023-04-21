"""
Отложенный старт для обновления данных
"""
import schedule, time, configJson, cacheData

def runup():
    preference = configJson.configScheduler()
    cron = f'schedule.every().{preference.schedule_type_value}.at.{preference.schedule_at_time_value}.do({cacheData.request_data})' \
           f'\nschedule.every({int(preference.schedule_period_query_value)}.{preference.schedule_period_time_type_value}.do({cacheData.request_data})'
    exec(cron)
    while True:
        schedule.run_pending()
        time.sleep(1)