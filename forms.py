"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, Length


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet's Name",
                       validators=[
                           InputRequired()
                       ])
    species = SelectField("Pet's Species",
                          choices=[
                              ('cat', 'Cat'),
                              ('dog', 'Dog'),
                              ('porcupine', 'Porcupine')
                          ],
                          validators=[
                              InputRequired()
                          ])
    photo_url = StringField('Add a link to image of pet',
                            validators=[
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
                      validators=[
                          InputRequired(),
                      ])
    notes = TextAreaField("Notes on pet",
                          validators=[
                              Optional(),
                              Length(min=5)
                          ])


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField('Add a link to image of pet',
                            validators=[
                                Optional(),
                                URL()
                            ])
    notes = TextAreaField("Notes on Pets",
                          validators=[
                              Optional(),
                              Length(min=5)
                          ])

    available = BooleanField("Available")
