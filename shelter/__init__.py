from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "admins.login" # set to "login", as if it were a 'url_for("admins.login")'
login_manager.login_message_category = "info" # how to set the message category, like a flash msg


def create_app(config_class=Config):
    app = Flask(__name__)
    
    import os
    os.system("source config.sh")
    
    app.config.from_object(config_class)
    
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    app.jinja_env.undefined = StrictUndefined
    
    from shelter.admins.routes import admins
    from shelter.animals.routes import animals_bp
    from shelter.main.routes import main
    from shelter.errors.handlers import errors

    app.register_blueprint(admins)
    app.register_blueprint(animals_bp)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app