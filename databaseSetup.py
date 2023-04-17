"""
Подготовка базы данных
"""
import psycopg2, configJson
def setup_connection():
    try:
        # подключение к базе данных
        preference = configJson.getData()
        conn = psycopg2.connect(host=preference['host'], user=preference['user'], password=preference['password'], dbname=preference['dbname'])
        return conn
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)