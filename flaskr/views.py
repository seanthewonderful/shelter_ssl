from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from flaskr import app
from flaskr.forms import RegisterAdmin, RegisterUser, LoginForm
import flaskr.crud


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
@app.route('/administrators')
def admin_init():
    
    register_form = RegisterAdmin()
    login_form = LoginForm()
    
    return render_template('admin/admin-init.html', 
                           register_form=register_form,
                           login_form=login_form)

@app.route('/register-admin', methods=["POST"])
def register_admin():
    """Register an Admin to the database"""
    
    username = request.form["username"].lower()
    password = request.form["password"]
    email = request.form["email"]
    clearance = request.form["clearance"]
    
    new_admin = flaskr.crud.create_admin(username=username,
                             password=password,
                             email=email,
                             clearance=clearance)
    
    if new_admin.status == "success":
        flash(f"New user created: {new_admin['new_admin'].username}")
        return redirect(url_for('admin_init'))
    else:
        flash(f"Error: new_admin={new_admin}")
        return redirect(url_for('admin_init'))

@app.route('/login-admin', methods=["POST"])
def login_admin():
    
    pass

@app.route('/users')
def user_init():
    
    return render_template('/user/user-init.html')

@app.route('/register-user')
def register_user():
    """Register a User to the database"""
    pass

"""Flask Manager routes"""
@login_manager.user_loader
def load_user(user_id):
    """LoginManager's user_loader"""
    # user_id should be type: str
    return flaskr.crud.get_user_by_id(user_id=user_id)

@login_manager.unauthorized_handler
def unauthorized():
    """Deny unauthorized users"""
    return "Sorry, you must be logged in to view this page"

