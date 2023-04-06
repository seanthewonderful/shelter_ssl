from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """The users table"""
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(50))
    email = db.Column(db.String(75))
    password = db.Column(db.String(100))
    zipcode = db.Column(db.String(5), nullable=True)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
class Admin(UserMixin, db.Model):
    """The Administrator table"""
    
    __tablename__ = "admins"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(50))
    email = db.Column(db.String(75))
    password = db.Column(db.String(100))
    clearance = db.Column(db.String(25))
    
    def __repr__(self) -> str:
        return super().__repr__()
    
class Animal(db.Model):
    """The parent class, Animal"""
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    species = db.Column(db.String(50))
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    description = db.Column(db.String(2000), nullable=True)
    
    # status = db.relationship("Status")

    def __repr__(self) -> str:
        return super().__repr__()
    

"""DB connect function"""
def connect_to_db(app, db=db):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRES_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_DEBUG'] = True
    db.app = app
    db.init_app(app)
    print("Connected to DB")
    
    
if __name__ == "__main__":
    os.system("source config.sh")
    from flaskr import app
    connect_to_db(app=app)
    