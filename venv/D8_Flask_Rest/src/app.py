from flask import Flask, request
from flask_restful import Resource, Api
import uuid

data = []

class Homer(Resource):
    def get(self):
        print(request)
        return {'data':data}
    def post(self):
        id = str(uuid.uuid4())
        name = request.form["name"]
        last_name = request.form['last_name']
        email = request.form['email']
        user ={"id":id, "name":name, "last_name":last_name, "email":email}
        data.append(user)
        return { 'data':user}


app = Flask(__name__)
api = Api(app)

api.add_resource(Homer, '/')



if __name__== '__main__':
    app.run(debug=True)