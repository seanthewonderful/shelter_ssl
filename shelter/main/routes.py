from flask import Blueprint, render_template

main = Blueprint('main', '__name__')

@main.route('/')
def home():
    """Homepage"""
    
    return render_template("homepage.html")