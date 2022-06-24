from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request


from models.item import ItemsModel

class Items(Resource):    
    @jwt_required()
    def get(self,name):
        item = ItemsModel.find_by_name(name)
        if item :
            return item.json()            
        return {"messge":"item dose not found"}
      
    @jwt_required()
    def post(self,name:str):
        item = ItemsModel.find_by_name(name)
        
        if item :
            return {'message' : 'Item with this name is already exists'}
        
        data = request.get_json()
        item = ItemsModel(name,data['price'])
        
        try:
            item.save_to_db()
        except:
            return {'message' : 'internal database error'}
        
        return item.json()
    
            
    @jwt_required()
    def delete(self,name):
        item = ItemsModel.find_by_name(name)
        if item:
            item.delete()
       
        return {'message':'Item deleted successfully'}
    
    @jwt_required()
    def put(self,name):
        data = request.get_json()        
        item = ItemsModel.find_by_name(name)               
        if item is None:
            item = ItemsModel(name = name,price=data['price'])            
        else:
            item.price = data['price']
        item.save_to_db()   
        return item.json()
            
class Itemslist(Resource):
    @jwt_required()
    def get(self):
        return {'Items':[x.json() for x in ItemsModel.query.all()]}
        
        
       