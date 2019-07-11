from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# local imports
from app.modules import form_class

class Test_form_class():

    def test_AdressForm_exists(self):
        """ cration of the class """
        assert hasattr(form_class, "AdressForm")
