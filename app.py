"""
Основное приложение
"""
import cacheData, schedule_refresh, threading
from flask import Flask
from flask_cors import CORS, cross_origin
from blueprints.doc import blueprint as doc

import configJson

app = Flask(__name__)
cors = CORS(app)

# Здесь лучше использовать стандартную библиотеку threading для второстепенного потока обновления данных, что я и делаю
schedule_thread = threading.Thread(target=schedule_refresh.runup(), daemon=True)


# Добавление рендеринга дефолтной index странички
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def catch_all():
    return app.send_static_file(preference.path_index_value)


# Запросы к серверу
@app.route('/getData', methods=['GET'])
@cross_origin()
def getData():
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/setData', methods=['POST'])
@cross_origin()
def setData():
    global data
    data = cacheData.request_data()
    return 'Success!'


# Документация swagger
app.register_blueprint(doc)

if __name__ == '__main__':
    app.run()
    data = cacheData.request_data()
    preference = configJson.configApp()
    schedule_thread.start()
