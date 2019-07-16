from flask import Flask
from flask import render_template

from toolbox.form import AddressForm
from toolbox.chatbot import Chatbot


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrette' # a refacturer

# user_raw_input = ""

@app.route('/form', methods=['GET', 'POST'])
def form():
    """
        controler 
    """  
    form = AddressForm()
    chatbot = Chatbot()
    
    if form.validate_on_submit():
        user_raw_input = form.text.data
        chatbot.answer(user_raw_input)
        return render_template(
            '/form.html',
            form=form,
            user_input=user_raw_input,
            parsed_text=chatbot.parsed,
            title=chatbot.name,
            link=chatbot.link,
            intro=chatbot.text,
            lat=chatbot.latitude,
            lgn=chatbot.longitude
        )       
    return render_template(
        '/form.html',
        form=form
    )

if __name__ == '__main__':
    app.run(debug=True)
    
    