from flask import (Flask, render_template, redirect, request, url_for, flash, jsonify)
from flask_login import login_user, logout_user, login_required, current_user
from shelter import app
from shelter.forms import (RegisterAdmin, RegisterUser, LoginForm, NewAnimalForm)
import shelter.crud as crud
from werkzeug.security import check_password_hash
