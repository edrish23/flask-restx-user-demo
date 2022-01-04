from flask import Blueprint
from flask_restx import Api

from user_api.user import api as user_ns

blueprint = Blueprint('user_api_v1', __name__, url_prefix='/api/v1/')
api = Api(blueprint,
          title='user demo API v1',
          version='1.0',
          description='This is version 1.0 for user demo Api',
          )

api.add_namespace(user_ns)

