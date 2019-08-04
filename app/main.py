from flask import Flask, render_template, request, jsonify

from toolbox.form import AddressForm
from toolbox.chatbot import Chatbot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrette' # a refacturer

@app.route('/form', methods=['GET', 'POST'])
def form():
    """
        controler 
    """ 
    chatbot = Chatbot()    
    if request.method == 'POST':
        user_input = request.form.get("userInput")        
        chatbot.answer(user_input) 

        return jsonify(
            address=chatbot.address,
            title=chatbot.name,
            link=chatbot.link,
            intro=chatbot.text,
            lat=chatbot.latitude,
            lng=chatbot.longitude
        )

    else:
        return render_template(
        '/form.html',
        lat=40,
        lng=42
        ) 

@app.route('/test')   
def test():
    return render_template('pages/test_home.html')

if __name__ == '__main__':
    app.run(debug=True)

        
    
    