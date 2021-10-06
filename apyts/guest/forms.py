from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms import validators
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, ValidationError
from email import errors


class ContactForm(FlaskForm):
    name=StringField('Your name',validators=[DataRequired(), Length(min=4, max=100,message='Name length must be between %(min)d and %(max)d characters')], render_kw={"placeholder":"Your name"})
    email=StringField('Your email address',validators=[DataRequired(),Email(), Length(max=120) ], render_kw={"placeholder":"Your email address"})
    summary=TextAreaField('Short summary of work',validators=[DataRequired(),Length(min=10, max=400, message='Name length must be between %(min)d and %(max)d characters')], render_kw={"placeholder":"Short summary of work"})
    submit= SubmitField('Submit')

class GreetUserForm(FlaskForm):
    username = StringField('Enter Your Name',
                           validators=[DataRequired(), Length(min=5, max=64, message='Name length must be between %(min)d and %(max)d characters')])
    submit = SubmitField('Submit')
