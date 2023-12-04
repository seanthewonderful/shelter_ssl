from flask import Blueprint, render_template, request, jsonify
from shelter.animals.forms import NewAnimalForm
import shelter.crud as crud

animals_bp = Blueprint('animals_bp', '__name__')

@animals_bp.route('/animals')
def animals():
    """Return all animals from DB"""
    
    form = NewAnimalForm()
    
    return render_template('animal/animals.html', form=form)


@animals_bp.route('/animals.json')
def animals_json():
    """Return all animals from db"""
    
    animals = crud.get_animal_dicts_list()
    
    return jsonify(animals)

@animals_bp.route('/add-animal', methods=["POST"])
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



