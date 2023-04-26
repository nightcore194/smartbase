"""
Подготовка базы данных
"""
import configJson, psycopg2, peewee

def setup_connection():
    try:
        # подключение к базе данных
        preference = configJson.configDB()
        db = peewee.PostgresqlDatabase(preference.db_name_value, user=preference.user_value, password=preference.password_value, host=preference.host_value) # создание бд
        conn = psycopg2.connect(preference.db_name_value, host=preference.host_value, user=preference.user_value, password=preference.password_value) # подключение к бд
        c = conn.cursor()
        c.execute("select * from information_schema.tables where table_name=%s", ('data',)) # полученние данных о существовании таблицы data в бд
        if(not bool(c)): # если нашей таблицы нет - мы ее создаем
            c.execute('''
                  CREATE TABLE data(
                  id_data INTEGER PRIMARY KEY ASC AUTOINCREMENT,
                  time_of_write timestamp NOT NULL,
        	      data_text TEXT NOT NULL
        	      )
                  ''')
        conn.commit()
        return conn
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)