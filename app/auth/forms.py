from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email = TextField('email', validators=[DataRequired(), Email()])
	password = PasswordField('password', validators=[DataRequired()])