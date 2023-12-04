from flask import Blueprint, render_template, redirect, flash, request, url_for, jsonify, current_app
from shelter.admins.forms import RegisterAdmin, LoginForm
import shelter.crud as crud
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

admins = Blueprint('admins', '__name__')

@admins.route('/administrators')
def admin_init():
    
    register_form = RegisterAdmin()
    login_form = LoginForm()
    
    return render_template('admin/admin-init.html', 
                           register_form=register_form,
                           login_form=login_form)

@admins.route('/register-admin', methods=["POST"])
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
        return redirect(url_for('admins.admin_init'))
    else:
        flash(f"Error: new_admin={new_admin}", 
              category="danger")
        return redirect(url_for('admins.admin_init'))
    
@admins.route('/account')
@login_required
def account():
    
    return render_template("account.html", 
                           title="Account")

@admins.route('/login-admin', methods=["POST"])
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
    
    # return redirect(url_for(next_page)) if next_page else redirect(url_for("admins.admin_init")) 

@admins.route('/logout')
def logout():
    
    logout_user()
    
    return redirect(url_for('main.home'))