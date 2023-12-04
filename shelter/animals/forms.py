from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

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