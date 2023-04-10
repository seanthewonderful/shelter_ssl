from flaskr.model import User, Admin, Animal, db
from werkzeug.security import generate_password_hash, check_password_hash

"""Admins"""

def create_admin(username, email, password, clearance):
    """Create an Admin object and commit to DB"""
    
    new_admin = Admin(username=username,
                      email=email,
                      password=generate_password_hash(password=password,
                                                      method="pbkdf2:sha256",
                                                      salt_length=16),
                      clearance=clearance)
    db.session.add(new_admin)
    db.session.commit()
    
    return {'code': 'success', 'admin': new_admin}

def get_admin_by_id(admin_id):
    """Returns Admin object from db with the provided id"""
    
    return Admin.query.filter_by(id=admin_id).first()


"""Users"""

def get_user_by_id(user_id):
    """Returns User object from db with the provided id"""

    return User.query.filter_by(id=user_id).first()

def create_user(username, email, password, zipcode):
    """Create a User object and commit to DB"""
    
    new_user = User(username=username,
                    email=email,
                    password=generate_password_hash(password=password, 
                                                    method="pbkdf2:sha256", 
                                                    salt_length=16),
                    zipcode=zipcode)
    db.session.add(new_user)
    db.session.commit()
    
    return {'code': 'success', 'user': new_user}

"""Animals"""

def create_animal(species, name, gender, age, description, adoption_status):
    """Create a new Animal object and commit to DB"""
    
    new_animal = Animal(species=species,
                        name=name, 
                        gender=gender,
                        age=age,
                        description=description,
                        adoption_status=adoption_status)
    
    db.session.add(new_animal)
    db.session.commit()
    
    return {'code': 'success', 'animal': new_animal}

def get_animal_by_id(animal_id):
    """Returns an Animal object from DB matching provided id"""
    
    return db.session.query(Animal).get(animal_id)
