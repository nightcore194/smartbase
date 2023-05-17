"""
Подготовка базы данных
"""
import server.configJson, peewee
from playhouse.migrate import *

def setup_connection():
    try:
        # подключение к базе данных
        preference = server.configJson.configDB()
        db = peewee.PostgresqlDatabase(preference.db_name_value, user=preference.user_value, password=preference.password_value, host=preference.host_value) # создание бд
        c = db.cursor()
        c.execute("select * from information_schema.tables where table_name=%s", ('data',)) # полученние данных о существовании таблицы data в бд
        if(not bool(c)): # если нашей таблицы нет - мы ее создаем
            c.execute('''
                  CREATE TABLE data(
                  id_data INTEGER PRIMARY KEY ASC AUTOINCREMENT,
                  time_of_data timestamp NOT NULL,
        	      data_text TEXT UNIQUE NOT NULL
        	      )
                  ''')
        c.execute("select * from information_schema.tables where table_name=%s", ('predict',)) # полученние данных о существовании таблицы predict в бд
        if (not bool(c)):  # если нашей таблицы нет - мы ее создаем
            c.execute('''
                          CREATE TABLE predict(
                          id_predict INTEGER PRIMARY KEY ASC AUTOINCREMENT,
                          time_of_predict timestamp NOT NULL,
                	      predict_data_text TEXT UNIQUE NOT NULL
                	      )
                          ''')
        db.commit()
        return db
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение
        print(e)