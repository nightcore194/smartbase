from flask import Blueprint
from flask_restx import Api
blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')

api_extension = Api(
    blueprint,
    title='Демонстрация возможностей Flask-RESTX',
    version='1.0',
    description='Инструкция к приложению для <b>статьи по Flask REST API\
    </b>, демонстрирующему возможности <b>пакета RESTX</b>, позволяющему\
    создавать масштабируемые сервисы и генерировать API документацию по ним',
    doc='/doc'
)