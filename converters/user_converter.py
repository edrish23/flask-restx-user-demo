from api_models.user_model import UserModel
from flask_restx import marshal


class UserConverters:
    def __init__(self):
        self._getting_users = UserModel.User_model

    def convert_to_get_user(self,final_response):
        return marshal(final_response, self._getting_users)

    def convert_to_post_user(self,final_response):
        return marshal(final_response, self._getting_users)
