from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('login',
                      'Авторизация')

login_model = namespace.model('login', {
    'TBA': fields.String(
        readonly=True,
        description='TBA'
    )
})

login_exp = {'TBA': 'TBA'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(login_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return login_exp