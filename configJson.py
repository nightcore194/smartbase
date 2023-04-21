"""
Получение данных из файла настроек в формате JSON
"""
import json

class configURL():
    def __init__(self):
        self.url = json.load(open('settings.json', 'r'))['url']
        self.header = json.load(open('settings.json', 'r'))['header']
        self.params = json.load(open('settings.json', 'r'))['params']

    @property
    def url_value(self):
        return self.url

    @property
    def header_value(self):
        return self.header

    @property
    def params_value(self):
        return self.params

class configScheduler():
    def __init__(self):
        self.schedule_period_query = json.load(open('settings.json', 'r'))['schedule_period_query']
        self.schedule_type = json.load(open('settings.json', 'r'))['schedule_type']
        self.schedule_time = json.load(open('settings.json', 'r'))['schedule_timing']
        self.schedule_at_time = json.load(open('settings.json', 'r'))['schedule_at_time']
        self.schedule_period_time_type = json.load(open('settings.json', 'r'))['schedule_period_time_type']
    @property
    def schedule_period_query_value(self):
        return self.schedule_period_query

    @property
    def schedule_type_value(self):
        return self.schedule_type

    @property
    def schedule_time_value(self):
        return self.schedule_time

    @property
    def schedule_at_time_value(self):
        return self.schedule_period_query

    @property
    def schedule_period_time_type_value(self):
        return self.schedule_period_time_type
class configDB():
    def __init__(self):
        self.db_name = json.load(open('settings.json', 'r'))['db_name']
        self.host = json.load(open('settings.json', 'r'))['host']
        self.user = json.load(open('settings.json', 'r'))['user']
        self.password = json.load(open('settings.json', 'r'))['password']

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

class configApp():
    def __init__(self):
        self.path_index = json.load(open('settings.json', 'r'))['path_index']
    @property
    def path_index_value(self):
        return self.path_index

class configModel():
    def __init__(self):
        self.path_data = json.load(open('settings.json', 'r'))['path_data']
        self.path_selected_feature = json.load(open('settings.json', 'r'))['path_selected_feature']
        self.model_path = json.load(open('settings.json', 'r'))['model_path']
    @property
    def path_data_value(self):
        return self.path_data

    @property
    def path_selected_feature_value(self):
        return self.path_selected_feature

    @property
    def model_path_value(self):
        return self.model_path