from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('predictData',
                      'Получение данных с сервера')

predictData_model = namespace.model('predictData', {
    'TBA': fields.String(
        readonly=True,
        description='TBA'
    )
})

predictData_exp = {'TBA': 'TBA'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(predictData_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return predictData_exp