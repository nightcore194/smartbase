"""
Получение данных с api в формате json
"""
import server.configJson, requests, pandas
from dataHandlerFacade import data_handler

def request_data():
    try:
        preference = server.configJson.configURL()
        head = { "AccessToken": requests.post(url=preference.url_value+'login/login', params=preference.params_login_value)["Account"]["AccessToken"] } # здесь реализуем авторизацию и получение токена в отдельный dict
        data = requests.get(url=preference.url_value+'dynamicApi/execute', headers=head, params=preference.body_value).json() # запрос на полученние данных
        df = pandas.read_json(str(data))
        df.to_csv('model/data_input_prediction/work.csv', encoding='utf-8', index=False)
        data_handler()
        return data
    except Exception as e:
        print(e)
        return 'Error!'