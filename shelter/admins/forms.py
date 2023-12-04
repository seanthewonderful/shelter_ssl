from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, EmailField, SubmitField
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