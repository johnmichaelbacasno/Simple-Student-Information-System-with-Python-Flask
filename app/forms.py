from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, NumberRange

class StudentForm(FlaskForm):
    id = StringField(
        label=('ID Number'),
        validators=[
            DataRequired(),
            Regexp(r'\d\d\d\d-\d\d\d', message='Pattern must be dddd-dddd.')],
        render_kw={
            'type':'text',
            'placeholder':'e.g. 0000-0000'
            }
        )
    
    first_name = StringField(
        label=('First Name'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )
    
    middle_name = StringField(
        label=('Middle Name'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )
    
    last_name = StringField(
        label=('Last Name'), 
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )
    
    course = SelectField(
        label=('Course'),
        choices=[('', '-- Select --')],
        validators=[
            DataRequired()],
        render_kw={}
        )
    
    year = IntegerField(
        label=('Year Level'),
        validators=[
            DataRequired(),
            NumberRange(min=1, max=5, message='Value must be between 1 to 5.')
            ],
        render_kw={
            'type': 'number',
            'placeholder': '1 - 5',
            'min': '1',
            'max': '5'
            }
        )
    
    birth_date = DateField(
        label=('Birth Date'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'date'
            }
        )
    
    birth_place = StringField(
        label=('Birth Place'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )
    
    sex = SelectField(
        label=('Sex'),
        choices=[
            ('', '-- Select --'),
            ('Male', 'Male'),
            ('Female', 'Female')
            ],
        validators=[
            DataRequired()
            ],
        render_kw={}
        )
    
    gender = StringField(
        label=('Gender'),
        validators=[
            DataRequired()],
        render_kw={
            'type': 'text'
            }
        )
    
    civil_status = SelectField(
        label=('Civil Status'),
        choices=[
            ('', '-- Select --'),
            ('Single', 'Single'),
            ('Married', 'Married'),
            ('Divorced', 'Divorced'),
            ('Widowed', 'Widowed')
            ],
        validators=[DataRequired()],
        render_kw={}
        )
    
    citizenship = StringField(
        label=('Citizenship'),
        validators=[
            DataRequired()],
        render_kw={
            'type': 'text'
            }
        )
    
    address = StringField(
        label=('Address'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )
    
    contact_number = StringField(
        label=('Contact Number'),
        validators=[
            DataRequired()
            ],
        render_kw={
            'type': 'text'
            }
        )

    submit = SubmitField(label=('Submit'))

class CourseForm(FlaskForm):
    code = StringField(
        label=('Code'),
        validators=[
            DataRequired()],
        render_kw={'type': 'text'}
        )
    
    name = StringField(
        label=('Name'),
        validators=[DataRequired()],
        render_kw={'type': 'text'}
        )
    
    college = SelectField(
        label=('College'),
        choices=[('', '-- Select --')],
        validators=[DataRequired()],
        render_kw={}
        )
    
    submit = SubmitField(label=('Submit'))

class CollegeForm(FlaskForm):
    code = StringField(
        label=('Code'),
        validators=[
            DataRequired()],
        render_kw={'type': 'text'}
        )
    
    name = StringField(
        label=('Name'),
        validators=[DataRequired()],
        render_kw={'type': 'text'}
        )
    
    submit = SubmitField(label=('Submit'))