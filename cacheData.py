"""
Получение данных с api в формате json
"""
import configJson, requests, pandas
from dataHandlerFacade import data_handler

def request_data():
    try:
        preference = configJson.configURL()
        data = requests.get(url=preference.url_value, headers=preference.header_value, params=preference.params_value).json()
        df = pandas.read_json(str(data))
        df.to_csv('model/data_input_prediction/work.csv', encoding='utf-8', index=False)
        data_handler()
        return data
    except Exception as e:
        print(e)
        return 'Error!'



