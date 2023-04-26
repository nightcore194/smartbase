"""
Модель представления БД
"""
import databaseSetup, peewee
# реализация струткуры ORM
# соединение с базой
class BaseModel(peewee.Model):
    class Meta:
        database = databaseSetup.setup_connection()

# Определяем модель данных(в качестве примера взял базу данных, которую описал в коде ранее)
class Data(BaseModel):
    time_of_write = peewee.AutoField(column_name=' time_of_write')
    data_text = peewee.TextField(column_name='data_text', null=True)
    class Meta:
        table_name = 'data'