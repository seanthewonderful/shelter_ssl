from shelter import db
from shelter.model import User, Admin, Animal
from werkzeug.security import generate_password_hash

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

def get_admin_by_username(username):
    """Returns Admin object from db with the provided username"""
    
    return Admin.query.filter_by(username=username).first()


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

def create_animal(species, name, gender, age, description, img_url):
    """Create a new Animal object and commit to DB"""
    
    new_animal = Animal(species=species,
                        name=name, 
                        gender=gender,
                        age=age,
                        description=description,
                        img_url=img_url)
    
    db.session.add(new_animal)
    db.session.commit()
    
    new_animal_dict = {}
    
    for column in new_animal.__table__.columns:
        new_animal_dict[column.name] = getattr(new_animal, column.name)
    
    return new_animal_dict

def get_all_animals():
    """Returns all animals from db"""
    
    return Animal.query.all()

def get_animal_dicts_list():
    """Returns a dictionary of animal object dictionaries"""
    
    animals = Animal.query.all()
    
    animals_list = []
    
    for animal in animals:
        animal_dict = {}
        for column in animal.__table__.columns:
            animal_dict[column.name] = getattr(animal, column.name)
        animals_list.append(animal_dict)
    
    return animals_list

def get_animal_by_id(animal_id):
    """Returns an Animal object from DB matching provided id"""
    
    return db.session.query(Animal).get(animal_id)
