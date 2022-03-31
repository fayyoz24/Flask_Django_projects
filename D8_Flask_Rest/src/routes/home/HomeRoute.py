from flask_restful import Resource
from flask import request
import uuid


data=[]

class HomeRoute(Resource):
    def get(self):
        print(request)
        return {'data':data}

    def post(self):
        id = str(uuid.uuid4())
        name = request.form["name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        user = {"id":id, "name":name, "last_name":last_name, "email":email}
        data.append(user)
        return {'data': user}

def find_obj_by_id(id):
    for data_obj in data:
        if data_obj["id"] == id:
            return data_obj
        else:
            return None


class HomeRoutewithID(Resource):
    def get(self, id):
        data_obj = find_obj_by_id(id)
        if(data_obj):
            return {"data":data_obj}
        else:
            return {"data": "Not Found"}, 404
    
    def put(self, id):
        data_obj = find_obj_by_id(id)
        if(data_obj):
            data_obj["name"] = request.form["name"]
            data_obj["last_name"] = request.form["last_name"]
            data_obj["email"] = request.form["email"]
            return {"data":data_obj}
        else:
           return {"data": "Not Found"}, 404

    def delete(self, id):
        data_obj = find_obj_by_id(id)
        if(data_obj):
            data.remove(data_obj)
            return {'data': 'Deleted'}
        else:
            return {'data' " Not Found"}, 404
    