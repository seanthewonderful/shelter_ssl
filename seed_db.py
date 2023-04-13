from flaskr.model import db, connect_to_db, User, Admin, Animal
from flaskr import app
from werkzeug.security import generate_password_hash
import os
import csv

os.system("dropdb ssl_adoption")
os.system("createdb ssl_adoption")
# with app.app_context():
#     db.create_all()
# connect_to_db(app)
app.app_context().push()
db.create_all()

admin1 = Admin(username="bloomers", email="a@a.com", password=generate_password_hash(os.environ["USER_PW"], method="pbkdf2:sha256", salt_length=16), clearance="brunch")
db.session.add(admin1)
db.session.commit()

with open('animals.csv') as animals:
    animal_file = csv.reader(animals, delimiter=',')
    line = 0
    for line in animal_file:
        if line == 0:
            line += 1
        else:
            new_animal = Animal(species=line[0],
                                name=line[1],
                                gender=line[2],
                                age=line[3],
                                img_url=line[4],
                                housebroken=line[5],
                                description=line[6])
            db.session.add(new_animal)
        
    db.session.commit()