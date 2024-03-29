from db import db

class ItemsModel(db.Model):
    __tablename__ = 'items'
        
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    
    def __init__(self,name,price):
        self.price = price
        self.name = name
        
    def json(self):
        return {'name':self.name,'price':self.price}
    
    @classmethod
    def find_by_name(cls,name):        
        return cls.query.filter_by(name=name).first()
   
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
        

                 
        
        
    