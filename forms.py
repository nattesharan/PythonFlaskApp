from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError
class ContactForm(Form):
    name = TextField('Name Of the Student',[validators.Required('Please enter your name')])
    gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    address = TextAreaField('Address')
    email = TextField('Enter Email', [validators.Required('Enter an email'),validators.Email('Please enter valid email address')])
    age = IntegerField('Age')
    language = SelectField('Languages', choices = [('CPP','C++'),('PY','Python'),('java','Java'),('js','JavaScript')])
    submit = SubmitField('Send')