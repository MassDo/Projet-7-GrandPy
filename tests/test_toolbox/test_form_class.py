# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# local imports
from app.toolbox import form

class Test_form_class():

    def test_AddressForm_exists(self):
        """ cration of the class """
        assert hasattr(form, "AddressForm")

    
