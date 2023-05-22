"""
Основное приложение
"""
from werkzeug.security import check_password_hash

import server.cacheData, server.schedule_refresh, threading, server.configJson
from flask import Flask, render_template, redirect, request, url_for
from flask_cors import CORS, cross_origin
from server.blueprints.doc import blueprint as doc
from server.forms import User
from server.databaseSetup import setup_connection
from flask_login import LoginManager, login_required, login_user
from models import User

# Старт приложения + запрос данных из апи, если это сделать в main, то просто пространство не даст увидеть его в фукциях фласка
preference = server.configJson.configApp()
app = Flask(__name__, template_folder=preference.path_index_value) # в template_folder указываем папку, где будем хранить templates-файлы
cors = CORS(app)
login_manager = LoginManager(app)
data = server.cacheData.request_data()
db = setup_connection()
# Здесь лучше использовать стандартную библиотеку threading для второстепенного потока обновления данных
# как вариант можно рассмотреть потоки Celery(насчет Flask ошибка - у фласка есть только свой кривой шедулер)
schedule_thread = threading.Thread(target=server.schedule_refresh.runup, daemon=True)

# Документация swagger, доступ к ней по /doc/doc
app.register_blueprint(doc)

# Добавление рендеринга дефолтной index странички
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def catch_all(path):
    return render_template('index.html')

# Авторизация в системе
@login_manager.user_loader()
def load_user(user_id):
    return User().fromDB(user_id, db)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('login'))
    return redirect(url_for('/'))

# Запросы к серверу
@app.route('/getData', methods=['GET'])
@login_required
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
@login_required
@cross_origin()
def setData():
    global data
    data = server.cacheData.request_data()
    return 'Success!'

if __name__ == '__main__':
    app.run()
    schedule_thread.start()
