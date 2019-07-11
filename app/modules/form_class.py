# third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AdressForm(FlaskForm):
    texte = StringField("USER INPUT", validators=[DataRequired()]) # rempacer par variable
                                                                   # user_input
    submit = SubmitField("Envoyer")