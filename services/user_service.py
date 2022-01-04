from converters.user_converter import UserConverters
from models.users_model import *
from languages.user_ex import APIException
from validations.user_validation import UserValidation
import json

class UserAPIService:
    def __init__(self):
        
        self.user_conversion_obj = UserConverters()

    def get_user_record(self):
        try:
            final_data = User.query.all()
            final_response = self.user_conversion_obj.convert_to_get_user(final_response=final_data)
            return {"Response": True,"ReturnCode": 1,"Result": final_response,"Message": "Success"}
    
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)
    def add_user_record(self,input_data):
        
        try:
            FullName=input_data.get('FullName')
            Email=input_data.get('Email')
            Mobile=input_data.get('Mobile')
            DateOfBirth=input_data.get('DateOfBirth')
            Password=input_data.get('Password')

            isEmailValid = UserValidation.checkValidEmail(Email)

            if isEmailValid == False:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"Email not valid"}

            users = User.query.filter(User.Email == Email).first()

            if users is not None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"User with this email alredy exist"}
            
            new_user = User(FullName=FullName, Email=Email,Mobile=Mobile,DateOfBirth=DateOfBirth,Password=Password)
            db.session.add(new_user)
            db.session.commit()
            final_response = self.user_conversion_obj.convert_to_post_user(final_response=new_user)
            return {"Response": True, "ReturnCode": 1, "Result": final_response, "Message": "Success"}
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)

    def get_user_by_id(self,user_id):
        try:
            user = User.query.get(user_id)
            if user is None:
                return {"Response": False, "ReturnCode": 1, "Result": [], "Message": f"No Record found for this id"}
            final_response = self.user_conversion_obj.convert_to_get_user(final_response=user)
            return {"Response": True, "ReturnCode": 1, "Result": final_response, "Message": "Success"}
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)

    def update_user_by_id(self,input_data,user_id):
        try:
            user_to_update = User.query.get(user_id)
            if user_to_update is None:
                return {"Response": False, "ReturnCode": 1, "Result": [], "Message": f"No Record found for this id"}
        
            # print('test',book_to_update.title)
            user_to_update.FullName=input_data.get('FullName')
            user_to_update.Email=input_data.get('Email')
            user_to_update.Mobile=input_data.get('Mobile')
            user_to_update.DateOfBirth=input_data.get('DateOfBirth')

            isEmailValid = UserValidation.checkValidEmail(user_to_update.Email)

            if isEmailValid == False:
                return {"Response": False, "ReturnCode": 1, "Result": [], "Message": f"Email not valid"}
        
            db.session.commit()
            final_response = self.user_conversion_obj.convert_to_post_user(
                user_to_update)
            return final_response
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)

    def delete_user_by_id(self,user_id):
        try:
            user_to_delete = User.query.get(user_id)
            if user_to_delete is None:
                return {"Response": False, "ReturnCode": 1, "Result": [], "Message": f"No Record found for this id"}
            db.session.delete(user_to_delete)
            db.session.commit()

            return "User Deleted"
        
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)

    def user_login(self,input_data):
        
        try:
            Email=input_data.get('Email')
            Password=input_data.get('Password')

            if Email is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"Email Required"}
            if Password is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"Password Required"}
            user = User.query.filter(User.Email == Email, User.Password == Password).first()

            if user is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"Invalid Credentials"}
            
            final_response = self.user_conversion_obj.convert_to_get_user(final_response=user)
            return {"Response":True,"ReturnCode": 1,"Result": final_response,"Message": "Logine Success"}, 201
            
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)

    def user_password_change(self,input_data):
        try:
            OldPassword=input_data.get('OldPassword')
            NewPassword=input_data.get('NewPassword')
            ids=input_data.get('id')

            if ids is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"id Required"}
            if OldPassword is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"OldPassword Required"}
            if NewPassword is None:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"NewPassword Required"}

            user = User.query.get(ids)
            if user is None:
                return {"Response": False, "ReturnCode": 1, "Result": [], "Message": f"No Record found for this id"}
            if user.Password == OldPassword:
                user.Password = NewPassword
                db.session.commit()
                return {"Response":True,"ReturnCode": 1,"Result": [],"Message": "Change Password Succssfully"}
            else:
                return {"Response":False,"ReturnCode": 1,"Result": [],"Message": f"OldPassword Incorrect"}
        except KeyError as e:
            return APIException(json.dumps(e.__dict__), status=500)
        except Exception as e:
            return APIException(json.dumps(e.__dict__), status=500)
