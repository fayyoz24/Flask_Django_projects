from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request
from flask_sqlalchemy import SQLAlchemy
import uuid


db = SQLAlchemy()
app = Flask(__name__)
app.debug = True


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app) #initialize database
db.create_all(app=app)# create table

api = Api(app)

class User(db.Model):
    user_id = db.Column(db.String(32), primary_key = True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable = False, default=db.func.now())
    def to_json(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name, 
            'last_name': self.last_name,
            'email': self.email,
            'created_at': str(self.created_at)
        }

class Striver(Resource):
    def get(self):
        users = db.session.query(User).all()
        users = [user.to_json() for user in users]
        return {'data':users}

    def post(self):
    
        name = request.form["name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
       
        user = User(first_name=name, last_name=last_name, email=email)
        db.session.add(user) 
        db.session.commit() 
      
        return {'data': user.to_json()}

class HomeRoutewithID(Resource):
    def get(self, id):
        data_obj = db.session.query(User).filter(User.user_id == id).first()
        if(data_obj):
            return {"data":data_obj.to_json()}
        else:
            return {"data": "Not Found"}, 404
    
    def put(self, id):
        data_obj = db.session.query(User).filter(User.user_id == id).first()
        if(data_obj):
            for key in request.form.keys():
                setattr(data_obj, key, request.form[key])
            return {"data":data_obj.to_json()}
        else:
           return {"data": "Not Found"}, 404

    def delete(self, id):
        data_obj = db.session.query(User).filter(User.user_id == id).first()
        if(data_obj):
            db.session.delete(data_obj)
            db.session.commit()
            return {'data': 'Deleted'}
        else:
            return {'data' " Not Found"}, 404

api.add_resource(Striver, '/')
api.add_resource(HomeRoutewithID, '/a')