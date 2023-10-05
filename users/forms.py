from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, length
import re


def character_check(self, field):
    excluded_chars = "<&%"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")


def password_validate(self, field):
    p = re.compile(r'(?=.*\d)(?=.*[a-z])')
    if not p.match(field.data):
        raise ValidationError("Password must contain at least 1 digit and one lowercase character.")

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Email(), character_check])
    password = PasswordField(validators=[DataRequired(), character_check, length(min=8, max=15), password_validate])
    submit = SubmitField()

