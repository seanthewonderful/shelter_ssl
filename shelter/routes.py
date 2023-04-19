from flask import (Flask, render_template, redirect, request, url_for, flash, jsonify)
from flask_login import login_user, logout_user, login_required, current_user
from shelter import app
from shelter.forms import (RegisterAdmin, RegisterUser, LoginForm, NewAnimalForm)
import shelter.crud as crud
from werkzeug.security import check_password_hash

# login_manager = LoginManager(app)
# login_manager.init_app(app)

@app.route('/')
def home():
    """Homepage"""
    
    return render_template("homepage.html")

@app.route('/animals')
def animals():
    """Return all animals from DB"""
    
    form = NewAnimalForm()
    
    return render_template('animals.html', form=form)

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
    
    new_admin = crud.create_admin(username=username,
                                  password=password,
                                  email=email,
                                  clearance=clearance)
    
    if new_admin['code'] == "success":
        flash(f"New user created: {new_admin['admin'].username}", 
              category="success")
        return redirect(url_for('admin_init'))
    else:
        flash(f"Error: new_admin={new_admin}", 
              category="danger")
        return redirect(url_for('admin_init'))
    
@app.route('/account')
@login_required
def account():
    
    return render_template("account.html", 
                           title="Account")

@app.route('/login-admin', methods=["POST"])
def login_admin():
    """Log in an Admin"""
    
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    
    administrator = crud.get_admin_by_username(username=username)
    
    if administrator:
        if check_password_hash(administrator.password, password):
            login_user(administrator)
            # login_user(administrator, remember=request.form.get("remember"))
            # next_page = request.args.get("next")
            # new query string 
            return jsonify({ "code": 200, "username": administrator.username })
        else: 
            flash("Password incorrect.", category="warning")
            return jsonify({ "code": 401, "message": "Password incorrect" })
    else:
        flash("No Administrators found with that username.", 
              category="warning")
        return jsonify({ "code": 401, "message": "No administrators found with that username" })
    
    # return redirect(url_for(next_page)) if next_page else redirect(url_for("admin_init")) 

@app.route('/logout')
def logout():
    
    logout_user()
    
    return redirect(url_for('home'))

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
    
    new_user = crud.create_user(username=username,
                                password=password,
                                email=email, 
                                zipcode=zipcode)

    print(new_user['user'].email)
    
    if new_user['code'] == "success":
        flash(f"New user created: {new_user['user'].username}", category="success")
        return redirect(url_for('user_init'))
    else:
        flash(f"Error: new_user={new_user}", category="danger")
        return redirect(url_for('user_init'))
    

"""Animal data routes"""

@app.route('/animals.json')
def animals_json():
    """Return all animals from db"""
    
    animals = crud.get_animal_dicts_list()
    
    return jsonify(animals)

@app.route('/add-animal', methods=["POST"])
def add_animal():
    """Add a new animal to the DB and return data to render a card"""
    
    print("HIT add-animal")
    
    name = request.get_json().get("name")
    species = request.get_json().get("species")
    gender = request.get_json().get("gender")
    age = request.get_json().get("age")
    description = request.get_json().get("description")
    img_url = request.get_json().get("imgUrl")
    
    new_animal = crud.create_animal(name=name,
                                    species=species,
                                    gender=gender,
                                    age=int(age),
                                    description=description,
                                    img_url=img_url)
    
    return jsonify(new_animal)



