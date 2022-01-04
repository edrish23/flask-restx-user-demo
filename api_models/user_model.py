from flask_restx import fields, Model


class UserModel:
    InputPayLoad = Model(
    'InputPayLoad',
    {

        'FullName':fields.String(),
        'Email':fields.String(),
        'Mobile':fields.String(),
        'DateOfBirth':fields.String(),
        'Password':fields.String(),
        
    }
    )

    User_model = Model(
        'User_model',
        {
            'id': fields.Integer(),
            'FullName':fields.String(),
            'Email':fields.String(),
            'Mobile':fields.String(),
            'DateOfBirth':fields.String(),
            
        }

    )
  

    @staticmethod
    def paylaod(api):
        
        api.models[UserModel.InputPayLoad.name] = UserModel.InputPayLoad
        return UserModel.InputPayLoad

class UserLoginModel:

    LoginInputPayLoad = Model(
        'LoginInputPayLoad',
        {
            'Email':fields.String(),
            'Password':fields.String(),
        
        }
        )

    @staticmethod
    def payload(api):
        api.models[UserLoginModel.LoginInputPayLoad.name] = UserLoginModel.LoginInputPayLoad
        return UserLoginModel.LoginInputPayLoad

class UserPasswordchange:

    PasswordchangePayLoad = Model(
        'PasswordchangePayLoad',
        {
            'id': fields.Integer(),
            'OldPassword':fields.String(),
            'NewPassword':fields.String(),
        }
        )


    @staticmethod
    def payload(api):
        api.models[UserPasswordchange.PasswordchangePayLoad.name] = UserPasswordchange.PasswordchangePayLoad
        return UserPasswordchange.PasswordchangePayLoad

# class MetricsModel:
#     sortBy = Model('sortBy', {
#         'field': fields.String(attribute="MetricSortName"),
#         'order': fields.String(default="asc/desc"),
#     })

'''
InputPayLoad = Model('InputPayLoad', {
    'filter': fields.List(fields.Nested(MetricFilter)),
    'sort-by': fields.List(fields.Nested(MetricSortBy)),
    'limit': fields.Integer(),
    'start_date': fields.String(),
    'end_date': fields.String()
})


@staticmethod
def paylaod(api):
        api.models[MetricsModel.MetricFilter.name] = MetricsModel.MetricFilter
        api.models[MetricsModel.MetricSortBy.name] = MetricsModel.MetricSortBy
        api.models[MetricsModel.InputPayLoad.name] = MetricsModel.InputPayLoad
        return MetricsModel.InputPayLoad
'''
