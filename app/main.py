from flask import Flask
from flask import render_template

from toolbox.form import AddressForm
from toolbox.chatbot import Chatbot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrette' # a refactuer

user_raw_input = ""

@app.route('/form', methods=['GET', 'POST'])
def form():
    """
        controleur de l'application
    """
    form = AddressForm()
    if form.validate_on_submit():
        user_raw_input = form.text.data
        bot = Chatbot(user_raw_input)
        response = bot.text

#########################
#                       #
#  ===>  A FAIRE  <===  #
#                       #
#########################
    
    return render_template('/form.html', form=form, response=response)

if __name__ == '__main__':
    app.run(debug=True)