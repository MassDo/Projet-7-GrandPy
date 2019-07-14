# third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    """
        Instantiate simple form object that
        is used in the '/form' route.
    """
    text = StringField(" ", validators=[DataRequired()]) 
    submit = SubmitField("Envoyer")
