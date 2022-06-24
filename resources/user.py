import sqlite3
from flask_restful import Resource
from flask import request

from models.user import UserModel

class Useregister(Resource):
    def post(self):
        data = request.get_json()
        if UserModel.find_by_username(data['username']):
            return {"message": "user already exists"}
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message" : "user add successfully"}
    

 