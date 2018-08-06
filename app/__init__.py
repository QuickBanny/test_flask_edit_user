import os
from flask_moment import Moment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from config import Config 


app = Flask(__name__)
app.config.from_object(Config)


login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')


from app.models import User
login_manager.login_views = 'auth.add_user'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
