from flask_login import *
from flask import Blueprint
from backend.database import User
from flask import redirect , url_for

login_manage = Blueprint('login_manage', __name__)

login_manager = LoginManager()

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def error():
    return redirect(url_for('Home'))
