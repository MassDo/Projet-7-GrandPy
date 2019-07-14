from .parser import Parser
from .api_manager import ApiManager
class Chatbot:

    def __init__(self, user_input):
         
        text_parsed = Parser(user_input)
        text_parsed.tokenized()
        text_parsed.pop()

        self.text = "LE BOT: " + text_parsed.text

        data_finder = ApiManager(text_parsed.text)
        data_finder.place_finder()
        data_finder.articles_nearby()
        data_finder.get_intro()
        self.link = data_finder.link
        self.intro = data_finder.intro

# récupérer le name et addresse



#########################
#                       #
#  ===>  A FAIRE  <===  #
#                       #
######################### 