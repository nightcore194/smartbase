from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('getData',
                      'Получение данных с сервера')

getData_model = namespace.model('getData', {
    'TBA': fields.String(
        readonly=True,
        description='TBA'
    )
})

getData_exp = {'TBA': 'TBA'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(getData_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return getData_exp