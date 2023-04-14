from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from os import environ
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


from shelter import routes