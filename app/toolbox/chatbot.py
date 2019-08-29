import random

from .parser import Parser
from .api_manager import ApiManager

class Chatbot:
    """
        class that instanciate object that
        can respond to the user,
    """
    text_parsed_list = []
    proximity = 0
    
    def __init__(self):
        self.input = ""
        self.text = ""
        self.name = ""
        self.address = ""
        self.latitude = float()
        self.longitude = float()
        self.link = ""
        self.parsed = ""

    def answer(self, user_input):
        """
            return the bot answer modulate by the proximity
            parameter of the method ApiManager.get_intro()
        """ 
        # intro_name = [
            
        # ]
        intro_address = [
            "Humm, je pense que l'adresse que tu recherches est: ",
            "Alors... Je peux me tromper mais je me souviens d'une adresse à cet endroit: ",
            "Je trouve une adresse à cet endroit j'espere que c'est la bonne: "
        ]
        intro_text = [
            "Sais tu que ", 
            "Ah je me souviens d'une histoire: ",
            "Attend laisse moi réfléchir... AH oui une histoire sur ce lieu: "
        ]
        outro_text = [
            " ... Bon excuse moi minot mais je suis en retard pour ma sieste si tu veux la suite clique plutot ici: ",
            " ... Ah ! J'ai oublié de prendre mes pillules ! Tu m'excuseras mais si tu veux la suite de l'histoire c'est ici: ",
            " ... Ooups attends, j'ai encore la mémoire qui flanche, si tu veux la suite regarde plutot ici: "
        ]

        self.input = user_input            
        
        # Parsing
        text_parser = Parser(self.input)
        text_parser.tokenized()
        text_parser.pop()         
        self.parsed = text_parser.text
        # if this is the first time user ask for a place
        if self.parsed in Chatbot.text_parsed_list:
           Chatbot.proximity += 1
        # if the user asking for the same place
        else:
            Chatbot.text_parsed_list.append(self.parsed)
            Chatbot.proximity = 0                       
        
        # API data collection
        try:
            data_finder = ApiManager(self.parsed)
            data_finder.place_finder()
            data_finder.articles_nearby()
            self.name = data_finder.name
            self.address = random.choice(intro_address) + data_finder.address
            self.latitude = data_finder.latitude
            self.longitude = data_finder.longitude
 
            if Chatbot.proximity >= len(data_finder.articles_id):
                Chatbot.proximity = 0

            data_finder.get_intro(Chatbot.proximity)
            self.link = data_finder.link
            self.text = random.choice(intro_text) + data_finder.intro[0:200] + random.choice(outro_text)
        except:
            print("no result or error in answer method")
        # data into the template
        
        if self.text == "":
            self.text = "Désolé mon ptit j'ai la mémoire qui flanche\
 je n'ai pas d'histoires sur cet endroit..."



if __name__ == '__main__':
    