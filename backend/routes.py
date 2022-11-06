from flask import *
from backend.database import *
import re
import os
from passlib.hash import pbkdf2_sha256
from backend.login_manager import *

routes = Blueprint('routes' , __name__ , static_folder='static' , template_folder='templates')

@routes.route('/Login' , methods = [ 'GET' ,'POST'])
def Login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email = email).first()
        if user:
            password_db = user.password
            check = pbkdf2_sha256.verify(password , password_db)
            if check:
                login_user(user)
                return jsonify({'message':'success'})
            else:
                return jsonify({'message': 'Password Does Not Match!!'})
        else:  
            return jsonify({'message':'* User Not Found'})
    if request.method == "GET":
        return render_template('/webpage/login.html')

@routes.route('/', methods = ['GET' , 'POST'])
def Home():
    products = Product.query.filter().all()
    item = Body_Image.query.filter().all()
    return render_template('/webpage/home.html' , item = item , products = products)
    
@routes.route('/Email_Check')
def Email_Check():
    email = request.args.get('email')
    email_re = request.args.get('email_check')
    pattern = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    email_check  = User.query.filter_by(email = email).first()
    if not re.search(pattern , email) :
        return "Invalid Email"
    elif email != email_re:
        return "Email Does Not Match"
    elif email_check:
        return "Email Already Registered"
    elif len(email) == 0 or len(email_re) == 0:
        return "Please Fill All The Fields"
    else:
        return "True"

@routes.route('/check_user')
def check_user():
    if current_user.is_authenticated:
        return jsonify({'msg':'done'})
    else:
        return jsonify({'msg':'fail'})
@routes.route('/Logout')
@login_required
def Logout():
    Add_To_Cart.query.filter_by(user = current_user.email).delete()
    db.session.commit()
    logout_user()
    return redirect(url_for('Home'))
@routes.route('/Register' , methods = ['GET' , 'POST'])
def Register():
    if request.method == 'POST':  
        email = request.form['email']
        first = request.form['first']
        last = request.form['last']
        phone = request.form['phone']
        agreement = request.form['agreement']
        address = request.form['address']
        password = request.form['password']
        passowrd_check = request.form['password_check']
        if password != passowrd_check:
            return jsonify({'message': 'Password Does Not Match'})
        elif len(password) == 0 or len(passowrd_check) == 0:
            return jsonify({'message':'Please Fill Out All The Missing Fields'})
        else:
            password = pbkdf2_sha256.hash(password)
            user  = User(email , first , last , phone , agreement , address , password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return jsonify({'message':'You Had Registed'})
    if request.method == 'GET':
        return render_template('/webpage/register.html')
@routes.route('/Add_To_Cart/<int:id>' , methods = ['POST'])
@login_required
def add_to_cart(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            id = id
            quantity = 1        
            product = Product.query.filter_by(id = id).first()
            user = current_user.email
            counter = Add_To_Cart.query.filter_by(product_id = id , user = current_user.email).first()
            if counter:
                counter.quantity = counter.quantity + 1
                db.session.commit()
            else:     
                price = product.price                               
                add_cart = Add_To_Cart(user , id , quantity , price)             
                db.session.add(add_cart)
                db.session.commit()          
            item = Add_To_Cart.query.filter_by(user = current_user.email).all()
            length = 0
            for i in item:           
                length = length + i.quantity  
            return jsonify({'len':length})

@routes.route('/add-quantity/<int:id>/<int:quantity>' , methods = ['GET'])
def add_quantity(id , quantity):
    
    id = id
    
    quantity = quantity
    
    new_total = 0
    
    user = Add_To_Cart.query.filter_by(product_id = id , user = current_user.email).first()
    if user:
        user.quantity = user.quantity + 1
        db.session.commit()
    item = Add_To_Cart.query.filter_by(user = current_user.email).all()
    for i in item:            
        new_total = new_total + (i.price * i.quantity)
    return jsonify({'done':user.quantity, 'total' : new_total })
@routes.route('/minus-quantity/<int:id>/<int:quantity>' , methods = ['GET'])
def minus(id , quantity):
    id = id
    quantity = quantity
    total = 0
    user = Add_To_Cart.query.filter_by(product_id = id , user = current_user.email).first()
    if user:
        if user.quantity == 1:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg':'sds'})
        else:
            user.quantity = user.quantity - 1
            db.session.commit()
            item = Add_To_Cart.query.filter_by(user = current_user.email).all()
            for i in item:                                                                  
                total = total + (i.price * i.quantity)
            return jsonify({'done':user.quantity,'total' : total })
@routes.route('/length' , methods = ['GET'])
# @login_required  
def get_length():
    length = 0
    if current_user.is_authenticated:
        item = Add_To_Cart.query.filter_by(user = current_user.email).all()
        for i in item:
            length = length + i.quantity
        return jsonify({'len':length})
    else:
        return jsonify({'len':0})

@routes.route('/query')
# @login_required
def find():
    if current_user.is_authenticated:
        query = db.session.query(Add_To_Cart.product_id).filter_by(user = current_user.email).first()
        if query is None:
            return jsonify({'cart': 'Your Cart Is Empty!!'})
        else:
            return jsonify('good')
    else:
        return jsonify({'cart': 'Login First'})
# @routes.route('/cart_view' , methods = ['GET'])
# @login_required
# def Cart_View():
#     query = db.session.query(Add_To_Cart.product_id).filter_by(user = current_user.email).first()
#     user = Add_To_Cart.query.filter_by(user = current_user.email).all()
#     total = 0
#     if query is None:
#         return redirect(url_for('shop'))
#     else:
#         if user:    
#             item = Add_To_Cart.query.filter_by(user = current_user.email).all()
#             for i in item:                         
#                 total = total + (i.price * i.quantity)                                                            
#             return render_template('/webpage/cart.html' , user = user , total = total)

@routes.route('/remove-item-cart/<int:id>' , methods = ['GET'])
@login_required
def remove_item(id):
    cart = Add_To_Cart.query.filter_by(user = current_user.email).first()
    if cart:
        cart_view = Add_To_Cart.query.filter_by(product_id = id).first()
        db.session.delete(cart_view)
        db.session.commit()
        return jsonify({'msg':'delete success'})
@routes.route('/Shop')
# @login_required
def shop():
    products = Product.query.filter().all()
    length = 0     
    return render_template('/webpage/shop.html' , products = products)
@routes.route('/product_view/<int:id>')    
def get_product_view(id):
    oke = False
    direct = 'static/img/anhtrinew/anh-tri-real/Product/product_' + str(id)
    files = os.listdir(direct)
    # for i in files:
    #     if i.endswith('.mp4'):
    #         oke = True
    products = Product.query.filter_by(id = id).first()
    id = id
    description = products.description
    description_eng = products.description_eng
    name = products.product_name
    price = products.price
    return render_template('/product/product_view.html', id = id , description = description , name = name , description_eng = description_eng , files = files , direct = direct, price = price)

    