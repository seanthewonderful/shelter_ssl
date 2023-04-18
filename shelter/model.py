from dataclasses import dataclass
from flask_login import UserMixin
import os
from shelter import db, login_manager


"""Flask login_manager functions"""
# @login_manager.user_loader
# def load_user(user_id):
#     """LoginManager's user_loader"""
    
#     return User.query.get(int(user_id))

@login_manager.user_loader
def load_admin(admin_id):
    """And one for the Admins"""
    
    return Admin.query.get(int(admin_id))

@login_manager.unauthorized_handler
def unauthorized():
    """Deny unauthorized users"""
    
    return "Please login to view this page"

class User(db.Model, UserMixin):
    """The users table"""
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(50))
    password = db.Column(db.String(250))
    email = db.Column(db.String(75))
    zipcode = db.Column(db.String(5), nullable=True)
    
    def __repr__(self) -> str:
        return f"<User: {self.username}>"
    
class Admin(db.Model, UserMixin):
    """The Administrator table"""
    
    __tablename__ = "admins"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(50))
    password = db.Column(db.String(250))
    email = db.Column(db.String(75))
    clearance = db.Column(db.String(25))
    
    def __repr__(self) -> str:
        return f"<Admin: {self.username} clearance: {self.clearance}>"
    
@dataclass
class Animal(db.Model):
    """The parent class, Animal"""
    
    __tablename__ = "animals"
    
    # species: str
    # name: str
    # gender: str
    # age: int
    # img_url: str
    # description: str
    # housebroken: bool
    # adoption_status: bool
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    species = db.Column(db.String(50))
    name = db.Column(db.String(50), default="")
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer, nullable=True)
    img_url = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    housebroken = db.Column(db.Boolean, nullable=True)
    adoption_status = db.Column(db.Boolean, default=False)
    
    def as_dict(self):
        return {}

    def __repr__(self) -> str:
        return f"<Animal id:{self.id} species:{self.species}>"
    

"""DB connect function"""
def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRES_URI']
    app.config["SQLALCHEMY_ECHO"] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_DEBUG'] = True
    db.app = app
    db.init_app(app)
    print("Connected to DB")
    
    
# if __name__ == "__main__":
#     os.system("source config.sh")
#     connect_to_db(app)
    