"""
Основное приложение
"""
import cacheData, schedule_refresh, threading, configJson
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from blueprints.doc import blueprint as doc

preference = configJson.configApp()
app = Flask(__name__, template_folder=preference.path_index_value)
cors = CORS(app)
data = cacheData.request_data()

# Здесь лучше использовать стандартную библиотеку threading для второстепенного потока обновления данных, но как вариант можно рассмотреть потоки Flask
schedule_thread = threading.Thread(target=schedule_refresh.runup, daemon=True)

# Документация swagger, доступ к ней по /doc/doc
app.register_blueprint(doc)

# Добавление рендеринга дефолтной index странички
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def catch_all(path):
    return render_template('index.html')

# Запросы к серверу
@app.route('/getData', methods=['GET'])
@cross_origin()
def getData():
    global data
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

if __name__ == '__main__':
    app.run()
    schedule_thread.start()
