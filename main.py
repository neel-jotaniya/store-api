from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 
import sys

if sys.version_info[:2] >= (3, 8):  # pragma: no cover
    from collections.abc import Mapping
    from collections import Mapping
from sequrity import authenticate,identity
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

