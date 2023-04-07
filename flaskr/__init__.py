from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
from os import environ
from flaskr.model import connect_to_db

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
csrf = CSRFProtect(app)
app.jinja_env.undefined = StrictUndefined
connect_to_db(app)


from flaskr import views