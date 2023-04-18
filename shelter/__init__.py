from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
# from shelter.model import connect_to_db

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config['SQLALCHEMY_DATABASE_URI'] = environ['POSTGRES_URI']
app.config["SQLALCHEMY_ECHO"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = True
csrf = CSRFProtect(app)
app.jinja_env.undefined = StrictUndefined
db = SQLAlchemy(app)
# connect_to_db(app)
login_manager = LoginManager(app)
login_manager.login_view = "login" # set to "login", as if it were a 'url_for("login")'
login_manager.login_message_category = "info" # how to set the message category, like a flash msg


from shelter import routes