from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('setData',
                      'Обновление данных с сервера')

setData_model = namespace.model('setData', {
    'TBA': fields.String(
        readonly=True,
        description='TBA'
    )
})

setData_exp = {'TBA': 'TBA'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(setData_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return setData_exp