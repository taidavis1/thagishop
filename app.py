from flask import *
from backend.database import db
from backend.admin import *
from backend.login_manager import *
from backend.routes import *
from flask_sslify import SSLify


app = Flask(__name__)
        
db.init_app(app)
    
SSLify(app)
    
login_manager.init_app(app)

app.register_blueprint(admin_page)

app.register_blueprint(routes)

app.register_blueprint(login_manage)

app.config['SQLALCHEMY_DATABASE_URI'] = "" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(100)


if __name__ == '__main__':
    
    app.run()
