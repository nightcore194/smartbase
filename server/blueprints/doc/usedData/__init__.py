from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('usedData',
                      'Получение данных с сервера')

usedData_model = namespace.model('usedData', {
    'TBA': fields.String(
        readonly=True,
        description='TBA'
    )
})

usedData_exp = {'TBA': 'TBA'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(usedData_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return usedData_exp