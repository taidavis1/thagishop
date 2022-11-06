from flask import *
from backend.database import *
import random

admin_page = Blueprint('admin_page' , __name__ , static_folder='static' , template_folder='templates')

@admin_page.route('/Add_Product' , methods=[ 'GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return render_template('/product/add_product.html')
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_img = request.form['product_img']       
        description = request.form['description']
        description_eng = request.form['description_eng']
        product_code = random.randint(000000000,999999999)
        product_quantity = request.form['quantity']
        price = request.form['price']
        product = Product(product_name, product_img , str(description) , str(description_eng) , product_code , product_quantity , price)
        db.session.add(product)
        db.session.commit()
        flash(f'Add Successful')
        return redirect(url_for('add_product'))
@admin_page.route('/Add_Body_Image' , methods=[ 'GET', 'POST'])
def add_product_image():
    if request.method == 'GET':
        return render_template('/product/add_body_product.html')
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_img = request.form['product_img']
        product_img_des = request.form['product_img_des']       
        product = Body_Image(product_name , product_img , product_img_des)
        db.session.add(product)
        db.session.commit()
        flash(f'Add Successful')
        return redirect(url_for('add_product_image'))
@admin_page.route('/Admin')
def admin():
    products = Product.query.filter().all()
    if products == None:
        flash(f'No More Product In Data')
    return render_template('/admin/admin.html' , products = products)
@admin_page.route('/delete/<int:id>')
def delete(id):
    id = Product.query.filter_by(id = id).first()
    db.session.delete(id)
    db.session.commit()
    flash(f'Delete Successul')
    return redirect(url_for('admin'))
@admin_page.route('/delete_user/<int:id>')
def delete_user(id):
    db.session.delete(id)
    db.session.commit()
    flash(f'Delete Successful')
    return redirect(url_for('user'))

@admin_page.route('/product_img/<int:id>')
def get_img(id):
    img = Product.query.filter_by(id = id).first()
    return Response(img.product_img , mimetype= "jpeg")
@admin_page.route('/User-Info')
def user():
    user = User.query.filter().all()
    return render_template('/admin/user.html' , user = user)
@admin_page.route('/Body_Image_Info')
def body_img_info():
    bimg = Body_Image.query.filter().all()
    return render_template('/admin/bodyimg.html' , bimg = bimg)
@admin_page.route('/Edit/<int:id>' , methods = ['GET' , 'POST'])
def edit_body_img(id):
    body_img = Body_Image.query.filter_by(id = id).first()
    if request.method == 'POST':
        body_img.location_place = request.form['location_place']
        body_img.product_name = request.form['product_name']
        body_img.description = request.form['description']
        body_img.description_vn = request.form['description_vn']
        db.session.commit()
        flash(f'Edit Success')
        return redirect(url_for('body_img_info'))
    return render_template('/admin/edit_body.html' , id= id , location_place = body_img.location_place , product_name = body_img.product_name , description = body_img.description , description_vn = body_img.description_vn)
@admin_page.route('/Edit_Add_Product/<int:id>' , methods = ['GET' , 'POST'])
def edit_add(id):
    product = Product.query.filter_by(id = id).first()
    if request.method == 'POST':
        product.product_name = request.form['product_name']
        product.description = request.form['description']
        product.description_eng = request.form['description_eng']
        product.product_quantity = request.form['quantity']
        db.session.commit()
        flash(f'Edit Success')
        return redirect(url_for('admin'))
    return render_template('/admin/edit_product.html' , id= id , product_name = product.product_name , description = product.description ,description_eng = product.description_eng, quantity = product.product_quantity)