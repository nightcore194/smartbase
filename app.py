"""
Основное приложение
"""
import cacheData, schedule_refresh, threading
from flask import Flask, render_template

app = Flask(__name__)

# Здесь лучше использовать стандартную библиотеку threading для второстепенного потока обновления данных, что я и делаю
schedule_thread = threading.Thread(target=schedule_refresh.runup(), daemon=True)

# Добавление рендеринга дефолтной index странички
@app.route('/')
def index():
    return render_template('index.html')
# Запросы к серверу
@app.route('/getData', methods=['GET'])
def getData():
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/setData', methods=['POST'])
def setData():
    global data
    data = cacheData.request_data()
    return 'Success!'

if __name__ == '__main__':
    app.run()
    data = cacheData.request_data()
    schedule_thread.start()
