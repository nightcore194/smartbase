from flask import Blueprint
from flask_restx import Api
from server.blueprints.doc.getData import namespace as getData_ns
from server.blueprints.doc.setData import namespace as setData_ns
blueprint = Blueprint('swagger', __name__, url_prefix='/doc')

api_extension = Api(
    blueprint,
    title='Документация к Flask-серверу SmartBase',
    version='1.0',
    description='Документация к серверу <b>SmartBase</b>.',
    doc='/doc'
)
api_extension.add_namespace(getData_ns)
api_extension.add_namespace(setData_ns)