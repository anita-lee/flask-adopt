"""Forms for adopt app."""
from lib2to3.pgen2.token import OP
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet's Name",
                        validators = [
                            InputRequired()
                        ])
    species = StringField("Pet's Species",
                        validators = [
                            InputRequired()
                        ])
    photo_url = StringField('Add a link to image of pet',
                        validators = [
                            Optional(),
                            URL()
                        ])
    age = SelectField("Select Pets Age Category",
                        choices=[
                            ('baby', 'Baby'),
                            ('young', 'Young'),
                            ('adult', 'Adult'),
                            ('senior', 'Senior')
                            ],
                        validators = [
                            InputRequired(),
                        ])
    notes = TextAreaField("Notes on pet")

