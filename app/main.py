from flask import Flask
from flask import render_template

from toolbox.form import AddressForm
from toolbox.parser import Parser
from toolbox.api_manager import ApiManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrette' # a refactuer

user_raw_input = ""

@app.route('/form', methods=['GET', 'POST'])
def form():
    """
        controler 
    """
    form = AddressForm()
    
    if form.validate_on_submit():
        user_raw_input = form.text.data
        # Parsing
        text_parsed = Parser(user_raw_input)
        text_parsed.tokenized()
        text_parsed.pop()
        # API data collection
        data_finder = ApiManager(text_parsed.text)
        data_finder.place_finder()
        data_finder.articles_nearby()
        data_finder.get_intro(1)
        # data into the template
        bot_response = "PARSED TEXT" + text_parsed.text
        
        return render_template(
            '/form.html',
            form=form,
            bot_response=bot_response,
            link=data_finder.link,
            intro=intro,
            title=data_finder.name
            )
        
    
    return render_template(
        '/form.html',
        form=form
    )

if __name__ == '__main__':
    user_raw_input = "Elysée"
    app.run(debug=True)
    print("\nAddress\n", address, "\nlink\n ", link, "\ntitle\n ", title ,"\nintro\n", intro)