from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

def init_app(app):
    
    db.init_app(app)
    

class User(UserMixin , db.Model):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(200) , nullable = False)
    first = db.Column(db.String(200) , nullable = False)
    last = db.Column(db.String(200) , nullable = False)
    phone = db.Column(db.String(200) , nullable = False)
    address = db.Column(db.String(200) , nullable = False)
    agreement = db.Column(db.String(200) , nullable = False)
    password = db.Column(db.String(200) , nullable = False)
    
    def _init_ (self , email , first , last , phone , agreement ,address , password):
        self.email = email
        self.first = first
        self.last = last
        self.phone = phone
        self.agreement = agreement
        self.address = address
        self.password = password

class Body_Image(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    product_name = db.Column(db.String(200) , nullable = False)
    product_img =  db.Column(db.String(200) , nullable = False)
    product_img_des =   db.Column(db.String(200) , nullable = False)
    
    def __init__(self  , product_name , product_img , product_img_des):
        self.product_name = product_name
        self.product_img = product_img
        self.product_img_des = product_img_des

class Product(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    product_name = db.Column(db.String(200) , nullable = False)
    product_img = db.Column(db.String(200) , nullable = False)
    description = db.Column(db.String(200) , nullable = False)
    description_eng = db.Column(db.String(200) , nullable = False)
    product_code = db.Column(db.Integer , nullable = False)
    product_quantity = db.Column(db.String(200) , nullable = False)
    price = db.Column(db.Integer , nullable = True)
    
    def _init_ (self , product_name , product_img , description , description_eng , product_code , product_quantity , price):
       self.product_name = product_name
       self.product_img = product_img
       self.description = description
       self.description_eng = description_eng
       self.product_code = product_code
       self.product_quantity = product_quantity
       self.price = price
    
class Add_To_Cart(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user = db.Column(db.String(200) , nullable = False)
    product_id = db.Column(db.Integer , nullable = True)
    quantity = db.Column(db.Integer , nullable = True)
    price = db.Column(db.Integer , nullable = True)
    
    def _init_ (self, user , product_id , quantity , price):
        self.user = user
        self.product_id = product_id
        self.quantity = quantity  
        self.price = price 

class ProductManager(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user = db.Column(db.String(200) , nullable = False)
    product_name = db.Column(db.String(200) , nullable = True)
    quantity = db.Column(db.Integer , nullable = True)
    price = db.Column(db.Integer , nullable = True)
    
    def _init_ (self, user , product_name , quantity , price):
        self.user = user
        self.product_name = product_name
        self.quantity = quantity
        self.price = price