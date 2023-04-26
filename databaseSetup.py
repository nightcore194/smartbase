"""
Подготовка базы данных
"""
import psycopg2, configJson
def setup_connection():
    try:
        # подключение к базе данных
        preference = configJson.configDB()
        conn = psycopg2.connect(host=preference.host_value, user=preference.user_value, password=preference.password_value, dbname=preference.db_name_value)
        return conn
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)