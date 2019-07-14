import requests


class ApiManager:
    """
        Class that instanciate objects that can find from a raw sentence:

        => Address at postal format if the sentence describe a place.
        => Coodrinates of the address (latitude and longitude).
        => Wikipedia's articles and their intro text nearby the address.

        This class is using google and wikipedia APIs.      
    """
    def __init__(self, parsed_text):
        """
            Constructor.
        """
        self.parsed_text = parsed_text
        self.name = ""
        self.address = ""
        self.latitude = float()
        self.longitude = float()
        self.intro = ""
        self.link = ""
        self.articles_id = [] # List of the id of articles
                              # found nearby the place.

    def place_finder(self):
        """ 
            The method place_finder must implement the instances attributs
            from the instance attribut parsed_text and the google place API:
                => name
                => address
                => latitude
                => longitude         
        """       
        payload = {
            "input": self.parsed_text,
            "language": "fr",
            "fields": "formatted_address,name,geometry/location",
            "inputtype": "textquery",
            "key": "AIzaSyAVJ9UzNh0XIXQ3oT400XvlieLNsfY_2fk"

        }        
        response = requests.get(
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?',
            params=payload
        ).json()

        self.name = response['candidates'][0]['name']
        self.address = response['candidates'][0]['formatted_address']
        self.latitude = response['candidates'][0]['geometry']['location']['lat']
        self.longitude = response['candidates'][0]['geometry']['location']['lng']

    def articles_nearby(self):
        """
            Using wikimedia action API.
            Return a list of the pageid wikimedia API parameter 
            nearby 100 meters radius from the coordinates point.
            The list returned is ordered by ascendant distance 
            from the place coordinates
        """
        api_payload = {
            "action": "query",
            "list": "geosearch",
            "gscoord": "{}|{}".format(self.latitude, self.longitude), 
            "gsradius": 100,
            "gslimit": 10,
            "format": "json"                  
        }      
        response = requests.get(
            "https://fr.wikipedia.org/w/api.php?",
            params=api_payload
        ).json()  

        self.articles_id = [
            article["pageid"] for article in response["query"]["geosearch"]
        ]

    def get_intro(self, proximity=0):
        """
            Using wikimedia action API.
            return the intro paragraphe of an article
            find with the pageid from articles_id attribut.           

            the proxymity parameter is the index of articles_id
            proximity == 0 => closest article from place coordinates          
        """
        api_payload = {
            "action": "query",
            "prop": "extracts",
            "exintro":"exintro",
            "explaintext": "explaintext",
            "redirects": 1,
            "pageids": self.articles_id[proximity],
            "format": "json"                  
        } 
        response = requests.get(
            "https://fr.wikipedia.org/w/api.php?",
            params=api_payload
        ).json()
        
        self.intro = response["query"]["pages"][str(self.articles_id[proximity])]["extract"]