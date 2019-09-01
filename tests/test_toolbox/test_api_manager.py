"""
    test of the module api_manager
"""
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

 
class MockRequestsGetWiki:
    """
        Mock requests.get for wiki api use
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



class MockRequestGetWikiIntroProximityDefault:
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


class MockRequestGetWikiIntroProximity_one:
    """
        Mock requests.get for wiki api use
        to get intro for second article.
        this mock is used if we are using 
        the research of article via coordinates.
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
                    "7161912": {
                      "pageid": 7161912,
                      "ns": 0,
                      "title": "Palais de l'Élysée",
                      "extract": "texte descriptif d'intro proximité = 1"
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

def test_methode_place_finder_works(monkeypatch):  
    """ 
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

    # test de la fonction
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()

    assert search_obj.name == "Le Palais de L'Élysée"
    assert search_obj.address == "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France"
    assert search_obj.latitude == 48.8704156
    assert search_obj.longitude == 2.3167539

def test_articles_nearby_exist():
    """
        Test if search_articles_nearby method is created.
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "articles_nearby")

def test_articles_nearby_works(monkeypatch):  
    """     
        Using wikimedia action API.
        Return the pageid wikimedia API parameter 
        of the first article's page found 
        nearby 100 meters radius from the coordinates point.        
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

def test_get_inro_exist():
    """
        Test if the method exist
    """
    test_object = api_manager.ApiManager("user parsed text")
    assert hasattr(test_object, "get_intro")

def test_get_intro_works_default_proximity(monkeypatch):
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
    #patching for wiki intro
    monkeypatch.setattr(
        'requests.get',
        MockRequestGetWikiIntroProximityDefault
    )
    search_obj.get_intro()

    assert search_obj.intro == "texte descriptif d'intro"

# def test_get_intro_works_proximity_1(monkeypatch):
#     """
#         Use this test if you are searching articles via
#         coordinates.
#         Test if get_intro() implement ApiManager.intro
#         using the second element of ApiManager.articles_id
#         and the wiki API.
#     """    
#     # patching for place api    
#     monkeypatch.setattr(
#         'requests.get', 
#         MockRequestsGetPlace
#     ) 
#     search_obj = api_manager.ApiManager("Elysée")
#     search_obj.place_finder()
#     # patching for wiki api
#     monkeypatch.setattr(
#         'requests.get',
#         MockRequestsGetWiki
#     )
#     search_obj.articles_nearby()
#     #patching for wiki intro
#     monkeypatch.setattr(
#         'requests.get',
#         MockRequestGetWikiIntroProximity_one
#     )
#     search_obj.get_intro(1)

#     assert search_obj.intro == "texte descriptif d'intro proximité = 1"
    


