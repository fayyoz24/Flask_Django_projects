from flask_restful import Resource
from flask import request
import uuid
from utils.models.user import User
from utils.db import db


data=[]

class HomeRoute(Resource):
    def get(self):
        users = db.session.query(User).all()
        users = [user.to_json() for user in users]
        return {'data':users}

    def post(self):
  
        name = request.form["name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        user_id = str(uuid.uuid4())
        
        user = User(user_id = user_id, first_name=name, last_name=last_name, email=email)
        db.session.add(user) #Add user to the database
        db.session.commit() #Commit the changes to the database
        # data.append(user)
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
    