import parser
class ArticleFinder():
    """
        class that instanciate objects that can find from a raw sentence:

        => Address at postal format if the sentence describe a place.
        => Coodrinates of the address (latitude and longitude).
        => Wikipedia's articles and their intro text nearby the address.

        This class is using google and wikipedia APIs.      
    """


    def __init__ (self, text_raw): # définir le type des data
        """
            init method
        """
        self.text_raw = text_raw
        self.id = int()
        self.lat = float()
        self.lgn = float()
        self.address = ""
        self.intro = ""

        
    def search_address(self):
        """
            Implementation using the geocoding google api of the attributes:
            => address (str)
            => lat (float)
            => lgn (float)    
        """
        pass

    def search_article_nearby(self):
        """
            Using wikimedia action API.
            Return the pageid wikimedia API parameter 
            of the first article's page found 
            nearby 50 meters radius from the coordinates point.
        """
        pass

    def search_article_intro_from_pageid(pageids):
        """
            Using wikimedia action API.
            return the intro paragraphe
            take the pageid API parameter.
        """
        pass

