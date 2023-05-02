"""
Классы настроек в формате JSON
"""
import json, codecs

preference = json.load(open('./settings.json', 'r'))

# перегрузочные методы @property - автоматически сгенерированный метод для геттеров/сеттеров/делиттеров, запрос для получения данных делать к этому методу
# в любой строке кфг если возникнет ошибка с \, то заменить \ на \\, почему так возникает - https://sites.pitt.edu/~naraehan/python3/mbb6.html#:~:text=In%20Python%20strings%2C%20the%20backslash,r%22%20is%20a%20carriage%20return.
# Класс настроек для подключения к api
class configURL():
    def __init__(self):
        self.url = preference['req']['_url']  # url api, к которому подключаемся
        self.header = preference['req']['_header'] # заголовка запроса, прописываются в виде словаря, в настройках - в виде обьекта json
        self.params_login = preference['req']['_params_login'] # параметры запроса(тело), прописываются в виде словаря, в настройках - в виде обьекта json
        self.body = preference['req']['_body'] # параметры запроса(тело), прописываются в виде словаря, в настройках - в виде обьекта json

    @property
    def url_value(self):
        return self.url

    @property
    def header_value(self):
        return self.header

    @property
    def params_login_value(self):
        return self.params_login

    @property
    def body_value(self):
        return self.body

# Класс настроек для отложенного запуск скрипта, пока прописываю под библиотеку schedule
class configScheduler():
    def __init__(self):
        self.schedule_period_query = preference['schedule']['_period_query'] # период опроса в указанном значении(в нашем случае в часах)

    @property
    def schedule_period_query_value(self):
        return self.schedule_period_query


# Класс настроек для подключения к БД
class configDB():
    def __init__(self):
        self.db_name = preference['db']['_name'] # название бд
        self.host = preference['db']['_host'] # хост, на котором располагается БД
        self.user = preference['db']['_user'] # user, созданный внутри БД
        self.password = preference['db']['_password'] # password, созданный внутри бд

    @property
    def db_name_value(self):
        return self.db_name

    @property
    def host_value(self):
        return self.host

    @property
    def user_value(self):
        return self.user

    @property
    def password_value(self):
        return self.password

# Класс настроек для приложения Flask
class configApp():
    def __init__(self):
        self.path_index = preference['app']['_path_index'] # путь к папке, где располагаются html файлы
    @property
    def path_index_value(self):
        return self.path_index

# Класс настроек для подключаемой модели
class configModel():
    def __init__(self):
        self.path_data = preference['model']['_path_data'] # путь до данных для модели
        self.path_selected_feature = preference['model']['_path_selected_feature'] # путь до файла настроек модели
        self._path = preference['model']['_path'] # путь до модели
    @property
    def path_data_value(self):
        return self.path_data

    @property
    def path_selected_feature_value(self):
        return self.path_selected_feature

    @property
    def _path_value(self):
        return self._path