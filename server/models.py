"""
Модель представления БД
"""
import server.databaseSetup, peewee
# реализация струткуры ORM
# соединение с базой
class BaseModel(peewee.Model):
    class Meta:
        database = server.databaseSetup.setup_connection()

# Определяем модель данных(в качестве примера взял базу данных, которую описал в коде ранее)
class Data(BaseModel):
    id_data = peewee.AutoField(column_name='id_data')
    time_of_data = peewee.DateTimeField(column_name='time_of_data')
    data_text = peewee.TextField(column_name='data_text', null=True)
    class Meta:
        table_name = 'data'

class Predict(BaseModel):
    id_predict = peewee.AutoField(column_name='id_predict')
    time_of_predict = peewee.DateTimeField(column_name='time_of_predict')
    predict_data_text = peewee.TextField(column_name='predict_data_text', null=True)
    class Meta:
        table_name = 'predict'