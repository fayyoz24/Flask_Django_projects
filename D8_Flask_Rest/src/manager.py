from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask import request
import uuid
from routes.home.HomeRoute import HomeRoute, HomeRoutewithID
from utils.db import db
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app) #initialize database
    db.create_all(app=app)# create table
    api = Api(app)
    api.add_resource(HomeRoute, '/')
    api.add_resource(HomeRoutewithID, '/<string:id>')
    return app


# create_app()
# if __name__== '__main__':
#     app.run(debug=True)