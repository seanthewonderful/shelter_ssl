from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, SelectField, SubmitField, IntegerField, TextAreaField, RadioField)
from wtforms.validators import DataRequired


class RegisterAdmin(FlaskForm):
    """Form to register an Administrator"""
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    clearance = SelectField('Clearance Level', choices=[('sunrise', "Sunrise"), 
                                                        ('brunch', 'Brunch'),
                                                        ('sunset', 'Sunset'),
                                                        ('midnight', 'Midnight')]
                            )
    submit = SubmitField('Create Administrator')
    
class RegisterUser(FlaskForm):
    """Form to register a User"""
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Register!')
    
class LoginForm(FlaskForm):
    """Form to accept Administrator or User credentials"""
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class NewAnimalForm(FlaskForm):
    """Form to create a new Animal"""
    
    species = StringField('Species', validators=[DataRequired()])
    name = StringField('Name', render_kw={'placeholder': 'If unknown, enter "None"'}, validators=[DataRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female'])
    age = IntegerField('Age')
    description = TextAreaField('Description', render_kw={'placeholder': 'Briefly describe where the animal came from, its demeanor, any quirks, etc.'})
    adoption_status = SelectField('Adoption Status', choices=[('adopted', 'Adopted'),
                                                              ('available', 'Available for adoption')])
    submit = SubmitField('Register Animal')