from flask import Flask, render_template, redirect, request
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from flaskr import app
import crud


app = Flask()
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def home():
    """Homepage"""
    
    return render_template("homepage.html")

@app.route('/animals')
def show_animals():
    """Return all animals from DB"""
    
    pass


"""Login Routes n stuff"""
@login_manager.user_loader
def load_user(user_id):
    
    return crud.get_user_by_id(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    
    return "Sorry, you must be logged in to view this page"

