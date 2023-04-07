from flaskr.model import db, connect_to_db, User, Admin, Animal
from flaskr import app
import os

os.system("dropdb ssl_adoption")
os.system("createdb ssl_adoption")

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    os.system("source config.sh")
    from flaskr import app
    connect_to_db(app=app)