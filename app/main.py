from flask import Flask, render_template, request, jsonify

from app.toolbox.form import AddressForm
from app.toolbox.chatbot import Chatbot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrette' # a refacturer

@app.route('/', methods=['GET', 'POST'])
def home():
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
        return render_template('/pages/home.html') 

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)

        
    
    