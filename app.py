from flask import Flask,jsonify,request
from flask_restx import Api, Resource,fields
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from models import db
from user_namespace import blueprint as apis
# from services.user_service import UserAPIService
from flask import Flask
from flask_cors import CORS

# book_service_obj = BookAPIService()
basedir=os.path.dirname(os.path.realpath(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'store_user.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

api=Api(app,doc='/',title="A User demo API",description="A simple REST API for users")

CORS(app)




def register_extensions(app):
    db.init_app(app)
    db.app = app
    db.create_all()
    return app



app.register_blueprint(apis)
register_extensions(app)


if __name__ == "__main__":
    app.run(debug=True)
