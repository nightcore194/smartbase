"""
Подготовка базы данных
"""
import sqlite3

def setup():
    conn = sqlite3.connect('cacheData.db')
    c = conn.cursor()
    c.execute('''
          CREATE TABLE data
          (id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
          time_of_write timestamp NOT NULL,
	      data_text TEXT NOT NULL)
          ''' )
    conn.commit()
    conn.close()