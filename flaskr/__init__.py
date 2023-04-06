from flask import Flask
from os import environ
from flaskr.model import connect_to_db

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
connect_to_db(app)


from flaskr import views