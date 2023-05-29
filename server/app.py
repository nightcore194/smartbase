"""
Основное приложение
"""


import server.cacheData, server.schedule_refresh, threading, server.configJson
from server.blueprints.doc import blueprint as doc
from server.databaseSetup import setup_connection
from server.models import User, Predict, Used
from server.databaseWrite import used_write

from werkzeug.security import check_password_hash

from flask import Flask, render_template, redirect, request, url_for
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required


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
@app.route('/getData', methods=['GET'])# получение общих данных
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

@app.route('/setData', methods=['POST']) # обновление общих данных
@login_required
@cross_origin()
def setData():
    global data
    data = server.cacheData.request_data()
    return 'Success!'

@app.route('/predictData', methods=['POST']) # получение данных, спрогнозированных моделью
@login_required
@cross_origin()
def predictData():
    data_resp = db.session.query(Predict).fileter(Predict.novk == request.args.get('novk'), Predict.nosiom == request.args.get('nosiom'))
    response = app.response_class(
        response=data_resp,
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/usedData', methods=['POST']) # получение данных использованных, спрогнозированных моделью
@login_required
@cross_origin()
def usedData():
    used = db.session.query(Predict).fileter(Predict.no_siom == request.args.get('nosiom'), Predict.no_vk == request.args.get('novk'))
    used_write(used.no_vk, used.no_siom, used.match_predict)
    db.session.query(Predict).fileter(Predict.no_siom == request.args.get('nosiom'),
                                      Predict.no_vk == request.args.get('novk')).delete() # здесь мы удаляем обьекты, используемые в производстве, из таблицы прогнозов
    db.session.commit()
    data_resp = db.session.query(Used).all()
    response = app.response_class(
        response=data_resp,
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()
    schedule_thread.start()
