from flask_restx import Namespace,Resource
from services.user_service import UserAPIService
from flask import Flask
from api_models.user_model import UserModel,UserLoginModel,UserPasswordchange
from flask import request

user_service_obj = UserAPIService()

api=Namespace(name="users",description="A simple REST API for user Registartion and Login")

parser = api.parser()
parser.add_argument('user_id', location='headers',type=int)

@api.route('/')
class Users_get(Resource):

    def get(self):
        ''' Get all users '''
       
        response = user_service_obj.get_user_record()
        return response

@api.route('/register/')
class users_post(Resource):
    @api.expect(UserModel.paylaod(api))
    def post(self):
        ''' Create a new users '''
        
        request_payload = api.payload
        
        response = user_service_obj.add_user_record(request_payload)
        return response


@api.route('/<int:id>')
class UserResource(Resource):

    def get(self,id):

        ''' Get a user by id '''
        response = user_service_obj.get_user_by_id(user_id=id)

        return response, 200


@api.expect(parser)
@api.route('/updateprofile/')
class UserUpdates(Resource):
    @api.expect(UserModel.paylaod(api))
    def put(self):

        ''' Update a user'''
        user_id = request.headers.get('user_id')
        request_payload = api.payload
        response = user_service_obj.update_user_by_id(request_payload, user_id=user_id)

        return response, 200

@api.route('/removeprofile/')
@api.expect(parser)
class UserRemove(Resource):
    def delete(self):
        '''Delete a user'''
        user_id = request.headers.get('user_id')
        response = user_service_obj.delete_user_by_id(user_id=user_id)
        return response



@api.route('/login')
class UserLogin(Resource):
    @api.expect(UserLoginModel.payload(api))
    def post(self):
        '''user login '''
        request_payload = api.payload
        response = user_service_obj.user_login(request_payload)
        return response

@api.route('/changepassword')
class Passwordchange(Resource):
    @api.expect(UserPasswordchange.payload(api))
    def post(self):
        '''password change '''
        request_payload = api.payload
        response = user_service_obj.user_password_change(request_payload)
        return response
    

