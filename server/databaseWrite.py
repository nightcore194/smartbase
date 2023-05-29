"""
Запись данных в бд
"""
import time, server.models, server.databaseSetup, json

db = server.databaseSetup.setup_connection()
def data_write(data):
    # отправка запроса к ранее подлюченной БД
    dataModel = server.models.Data(time_of_write=time.strftime('%Y-%m-%d %H:%M:%S', 'utc'), data_text=data)
    db.session.add(dataModel)
    db.session.commit()

def predict_write(predict):
    # отправка запроса к ранее подлюченной БД
    predict_dump = json.loads(predict)
    mass = []
    for i in range(len(predict_dump['no_vk'])):
        mass.append(server.models.Predict(no_vk=predict_dump['no_vk'][str(i)],
                                          no_siom=predict_dump['no_siom'][str(i)],
                                          match_predict=predict_dump['class_HC'][str(i)]))
    db.session.add_all(mass)
    db.session.commit()

def used_write(no_vk, no_siom, match_predict):
    usedModel = server.models.Used(no_vk=no_vk, no_siom=no_siom, match_predict=match_predict)
    db.session.add_all(usedModel)
    db.session.commit()