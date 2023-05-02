"""
Обработка полученных данных в формате json
"""
import server.databaseWrite, server.configJson
from server.model.server_model import MainPipeline
def data_handler(): # здесь передаем данные, получаемые с сервера smartbase, формат определяется в соответствии с требованиями
    preference = server.configJson.configModel()
    try:
        df_pred = MainPipeline(path_data=preference.path_data_value, path_selected_features=preference.path_selected_feature_value, model_path=preference.model_path_value, model_type='classification')
        df_pred = df_pred.to_json(orient='columns')
        server.databaseWrite.data_write(df_pred)
    except Exception as e:
        return e