from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class AddUserForm(FlaskForm):
    email = TextField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Add user')

    def validate(self):
        if not super(AddUserForm, self).validate():
            return False

        if User.query.filter_by(email=self.email.data).first():
            self.email.errors.append('Email already.')
            return False
        return True


class EditUserForm(FlaskForm):
    email = TextField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    admin = BooleanField('Admin')
    submit = SubmitField('Edit')

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_email(self, field):

        if User.query.filter_by(email=field.data).first() and \
                field.data != self.user.email:
            self.email.errors.append('Email already.')
            return False
        return True