from flask import (Flask, render_template, redirect, request, url_for, flash)
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from flaskr import app
from flaskr.forms import (RegisterAdmin, RegisterUser, LoginForm, NewAnimalForm)
import flaskr.crud


login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    """Homepage"""
    
    return render_template("homepage.html")

@app.route('/animals')
def animals():
    """Return all animals from DB"""
    
    form = NewAnimalForm()
    
    return render_template('animals.html', form=form)

@app.route('/register-animal', methods=["POST"])
def register_animal():
    """Register a new animal to the DB"""
    
    species = request.form.get("species")
    name = request.form.get("name", "None")
    gender = request.form.get("gender")
    age = request.form.get("age", 0)
    description = request.form.get("description")
    adoption_status = request.form.get("adoption_status")
    
    print(type(age)) # --> it's a str
    new_animal = flaskr.crud.create_animal(species=species,
                                           name=name,
                                           gender=gender,
                                           age=age,
                                           description=description,
                                           adoption_status=adoption_status)   
    if new_animal['code'] == 'success':
        flash(f"New {species} added to database")
        return redirect(url_for('animals'))
    else:
        flash("Erroneous")
        return redirect(url_for('animals'))

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
    
    if new_admin['code'] == "success":
        flash(f"New user created: {new_admin['admin'].username}")
        return redirect(url_for('admin_init'))
    else:
        flash(f"Error: new_admin={new_admin}")
        return redirect(url_for('admin_init'))

@app.route('/login-admin', methods=["POST"])
def login_admin():
    
    pass

@app.route('/users')
def user_init():
    """Initial User Portal"""
    
    register_form = RegisterUser()
    login_form = LoginForm()
    
    return render_template('/user/user-init.html',
                           register_form=register_form,
                           login_form=login_form)

@app.route('/register-user', methods=["POST"])
def register_user():
    """Register a User to the database"""
    
    username = request.form["username"].lower()
    password = request.form["password"]
    email = request.form["email"]
    zipcode = request.form["zipcode"]
    
    new_user = flaskr.crud.create_user(username=username,
                                       password=password,
                                       email=email, 
                                       zipcode=zipcode)
    
    print(new_user)
    print(new_user['user'].email)
    
    if new_user['code'] == "success":
        flash(f"New user created: {new_user['user'].username}")
        return redirect(url_for('user_init'))
    else:
        flash(f"Error: new_user={new_user}")
        return redirect(url_for('user_init'))
    
@app.route('/login-user', methods=["POST"])
def login_user():
    
    pass

"""Flask Manager routes"""
@login_manager.user_loader
def load_user(user_id):
    """LoginManager's user_loader"""
    
    return flaskr.crud.get_user_by_id(user_id=user_id)

@login_manager.unauthorized_handler
def unauthorized():
    """Deny unauthorized users"""
    return "Sorry, you must be logged in to view this page"

