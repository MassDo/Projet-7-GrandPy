
"""
    test of the module api_manager
"""
import pytest

from app.toolbox import api_manager


class MockRequestsGetPlace:
    """
        Mock requests.get for the api place.
    """
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Return the simulate json that will
            be returned by the api in real situation.
        """
        return {
           "candidates" : [
                {
                   "formatted_address" : "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France",
                   "geometry" : {
                        "location" : {
                           "lat" : 48.8704156,
                           "lng" : 2.3167539
                        }
                   },
                   "name" : "Le Palais de L'Élysée"
                }
           ],
           "status" : "OK"
        }


class MockRequestsGetPlaceEmpty:
    """
        Mock requests.get for the api place with empty return data.
    """
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Return the simulate json that will
            be returned by the api in real situation
            with empty data.
        """
        return {
           "candidates" : [],
           "status" : "OK"
        }

 
class MockRequestsGetWiki:
    """
        Mock requests.get for wiki api use with,
        correct data returned. 

    """    
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Return the simulate json that will
            be returned by the api in real situation
            for Palais de l'Élysée search.
        """
        return {
            "batchcomplete": "",
            "continue": {
                "sroffset": 1,
                "continue": "-||"
            },                
            "query": {
                "searchinfo": {
                    "totalhits": 3628
                },
                "search": [
                    {
                    "ns": 0,
                    "title": "Palais de l'Élysée",
                    "pageid": 38724,
                    "size": 186587,
                    "wordcount": 23333,
                    "snippet": "voir <span class=\"searchmatch\">Élysée</span>. <span class=\"searchmatch\">Palais</span> <span class=\"searchmatch\">de</span> <span class=\"searchmatch\">l'Élysée</span> La cour et l'entrée du <span class=\"searchmatch\">palais</span> <span class=\"searchmatch\">de</span> <span class=\"searchmatch\">l'Élysée</span>. modifier - modifier le code - modifier Wikidata Le <span class=\"searchmatch\">palais</span> <span class=\"searchmatch\">de</span> <span class=\"searchmatch\">l'Élysée</span>, dit",
                    "timestamp": "2019-08-01T04:19:47Z"
                    }
                ]
            }
        }


class MockRequestsGetWikiIncorrectReturn:
    """
        Mock requests.get for wiki api use with,
        correct data returned. 

    """    
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Return the simulate incorrect json that will
            be returned by the api
        """
        return {
            "batchcomplete": "",
            "continue": {
                "sroffset": 1,
                "continue": "-||"
            }
        }


class MockRequestGetWikiIntro:
    """
        Mock requests.get for wiki api use
        to get intro for first article
    """    
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Return the simulate json that will
            be returned by the api in real situation.
        """
        return {
            "batchcomplete": "",
            "query": {
                "pages": {
                    "38724": {
                      "pageid": 38724,
                      "ns": 0,
                      "title": "Palais de l'Élysée",
                      "extract": "texte descriptif d'intro"
                    }
                }
            }
        }

class MockRequestGetWikiIntroEmptyData:
    """
        Mock requests.get for wiki api 
        returning corrupted data.
    """    
    def __init__(self, url, params=None):
        """
            Give the parameters to the mock
        """
        pass

    def json(self):
        """
            Simulate empty json for extrac key (introduction article
            of a wikipedia page) .
        """
        return {
            "batchcomplete": "",
            "query": {
                "pages": {
                    "38724": {
                      "pageid": 38724,
                      "ns": 0,
                      "title": "Palais de l'Élysée"
                    }
                }
            }
        }


def test_ApiManager_exist():
    """
        Test if class ApiManager is created.
    """
    assert hasattr(api_manager, "ApiManager")

def test_attributs_exist():
    """
        Test if attribut are created.
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "parsed_text")
    assert hasattr(test_object, "name")
    assert hasattr(test_object, "address")
    assert hasattr(test_object, "latitude")
    assert hasattr(test_object, "longitude")
    assert hasattr(test_object, "intro")
    assert hasattr(test_object, "link")
    assert hasattr(test_object, "articles_id")

def test_place_finder_exist():
    """
        Test if the instance method place_finder exit
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "place_finder")

# NEW
# Google Place API 
def test_methode_place_finder_works(monkeypatch):  
    """ 
        Google Place API connection test if correct data sent.

        The method place_finder must implement the instances attributs
        from the instance attribut parsed_text and the google place API:

            => name
            => address
            => latitude
            => longitude           
    """   
    # Patching du monkeypatch pour remplacer méthode requests.get 'app.toolbox.api_manager.requests.get'
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetPlace
    )

    # test de la méthode
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()

    assert search_obj.name == "Le Palais de L'Élysée"
    assert search_obj.address == "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France"
    assert search_obj.latitude == 48.8704156
    assert search_obj.longitude == 2.3167539

# Empty input
def test_place_finder_empty_input():
    """
        Test if a exception is raised if
        we give a empty text in input.
    """
    search = api_manager.ApiManager("")
    with pytest.raises(Exception, match="Cannot search place with empty text"):
        assert search.place_finder()

# Corrupted data in return from Google Place Api
def test_place_finder_corrupted_return_raise_Exception(monkeypatch):
    """
        Testing if a exception is raised for corrupted data
        from api json file.

        Also testing if the method return empty string for 
        the attributes name & address.
        And return value 0 for the attributes latitudes & longitude
    """

    # Patching of the corrupted data mock
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetPlaceEmpty
    )
    # test
    search_obj = api_manager.ApiManager("Elysée")
    with pytest.raises(Exception, match="invalid data from Api ... "):
        assert search_obj.place_finder()
        assert search_obj.name == ""
        assert search_obj.address == ""
        assert search_obj.latitude == 0
        assert search_obj.longitude == 0

def test_articles_nearby_exist():
    """
        Test if search_articles_nearby method is created.
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "articles_nearby")

# Wikipedia API
def test_articles_nearby_works(monkeypatch):  
    """  
        Wikimedia API connection test if correct data sent.

        Using wikimedia action API.
        Return the pageid wikimedia API parameter 
        of the first article's page found.         
    """     
    # patching for place api    
    monkeypatch.setattr(
        'requests.get', 
        MockRequestsGetPlace
    ) 
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()
    # patching for wiki api
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetWiki
    )
    search_obj.articles_nearby()

    assert search_obj.articles_id == [
        38724,
    ]   

# Empty input
def test_articles_nearby_empty_input():
    """
        Test if a exception is raised if
        we give a empty text in input.
    """
    search = api_manager.ApiManager("")
    with pytest.raises(
        Exception,
        match="Cannot search for article id if term of the research is empty"
        ):
        assert search.articles_nearby()

# Corrupted data in return from the wiki Api
def test_articles_nearby_corrupted_return(monkeypatch):
    """
        Testing if exception is raised for 
        corrupted json data wiki api return.
    """
       # patching for place api correct data return   
    monkeypatch.setattr(
        'requests.get', 
        MockRequestsGetPlace
    ) 
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()

    # patching for wiki api corrupted data
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetWikiIncorrectReturn
    )
    with pytest.raises(
        Exception,
        match="The data From wikipedia Api are corrupted"
        ):
        assert search_obj.articles_nearby()

def test_get_intro_exist():
    """
        Test if the method exist
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "get_intro")

# Wiki Api Intro text collection with correct json data
def test_get_intro_works_correct_data(monkeypatch):
    """
        Test if get_intro() implement ApiManager.intro
        using the first element of ApiManager.articles_id
        and the wiki API
    """    
    # patching for place api    
    monkeypatch.setattr(
        'requests.get', 
        MockRequestsGetPlace
    ) 
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()

    # patching for wiki api
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetWiki
    )
    search_obj.articles_nearby()

    #patching for wiki intro with valids json data.
    monkeypatch.setattr(
        'requests.get',
        MockRequestGetWikiIntro
    )
    search_obj.get_intro()

    assert search_obj.intro == "texte descriptif d'intro"

# Empty input data
def test_get_intro_empty_input_raise_exception():
    """
        Test if get_intro() with empty wiki article id
        raise an eception
    """
    search = api_manager.ApiManager("")

    with pytest.raises(IndexError):
        assert search.get_intro()

# No intro in json data from wiki api
def test_get_intro_empty_json_result(monkeypatch):
    """
        Test if a exception is raise if corrupted 
        json data from api.

        Also the attribut intro of the ApiManager instatiation
        must be a empty string in this case in order to trigger
        the "no result" bot response buble. 
    """ 
    # patching for place api    
    monkeypatch.setattr(
        'requests.get', 
        MockRequestsGetPlace
    ) 
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()

    # patching for wiki api
    monkeypatch.setattr(
        'requests.get',
        MockRequestsGetWiki
    )
    search_obj.articles_nearby()

    #patching for wiki intro with empty json data.
    monkeypatch.setattr(
        'requests.get',
        MockRequestGetWikiIntroEmptyData
    )
    
    with pytest.raises(Exception, match="The intro data from wiki Api is corrupted or empty..."):
        assert search_obj.get_intro()
        assert search_obj.intro == ""


    

