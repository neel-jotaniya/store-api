from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 

from security import authenticate,identity
from resources.item import Items, Itemslist
from resources.user import Useregister

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key= 'super-thunder'

api = Api(app)
jwt = JWT(app,authenticate,identity)

api.add_resource(Items,'/items/<string:name>')
api.add_resource(Itemslist,'/items')
api.add_resource(Useregister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    app.run(port=5000, debug= True)
    
    
    

