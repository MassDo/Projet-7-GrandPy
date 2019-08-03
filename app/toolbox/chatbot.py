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
            self.address = data_finder.address
            self.latitude = data_finder.latitude
            self.longitude = data_finder.longitude
 
            if Chatbot.proximity >= len(data_finder.articles_id):
                Chatbot.proximity = 0

            data_finder.get_intro(Chatbot.proximity)
            self.link = data_finder.link
            self.text = "Sais tu que " + data_finder.intro
        except:
            print("pas de résultat")
        # data into the template
        
        if self.text == "":
            self.text = "Désolé mon ptit j'ai la mémoire qui flanche\
 essaye un autre endroit..."



if __name__ == '__main__':
    chatbot = Chatbot()
    chatbot.answer("Elysée")
    print(
        chatbot.address,
        chatbot.name,
        chatbot.link,
        chatbot.text,
        chatbot.latitude,
        chatbot.longitude
    )