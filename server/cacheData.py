"""
Получение данных с api в формате json
"""
import server.configJson, requests, pandas, time, codecs
from server.dataHandlerFacade import data_handler
from server.databaseWrite import data_write

def request_data():
    try:
        preference = server.configJson.configURL() # обьект класса настроек для
        data = requests.post(url=preference.url_value + 'dynamicApi/execute', headers=preference.header_value,
                             json=preference.body_value)  # запрос на полученние данных
        if data.status_code != 200:
            preference.header_value.setter("AccessToken", requests.post(url=preference.url_value + 'login/login',
                                                                        json=preference.params_login_value).json()["Account"]["AccessToken"])  # здесь реализуем авторизацию и получение токена в отдельный dict
            data = requests.post(url=preference.url_value + 'dynamicApi/execute', headers=preference.header_value,
                                 json=preference.body_value)  # запрос на полученние данных
        data.encoding = 'utf-8' # изменение кодировки
        data = data.json() # получение данных в формате json
        data_temp = data['eche'] # для записи в бд
        data_write(str(data))  # запись в бд
        for i in range(len(data_temp)):
            # преобразование данных в формат csv для модели
            df = pandas.read_json(str(data_temp[i]))
            df.to_csv(f'model/data_input_prediction/work{i}.csv', encoding='utf-8', index=False)
        data_handler()
        return data
    except Exception as e:
        print(e)
        return e