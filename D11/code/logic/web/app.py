from flask.cli import FlaskGroup
from api import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask import request
import uuid


db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app) #initialize database
db.create_all(app=app)# create table
api = Api(app)
cli = FlaskGroup(app)

if __name__=="__main__":
    cli()