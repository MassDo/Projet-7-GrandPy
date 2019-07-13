from app.modules import api_manager
 
def test_ApiManager_exist():
    """
        Test if class is created.
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
    class MockRequestsGet:
    
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
    
    # Patching du monkeypatch pour remplacer méthode requests.get
    monkeypatch.setattr(
        'app.modules.api_manager.requests.get',
        MockRequestsGet
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
                be returned by the api in real situation.
            """
            return {
                "batchcomplete": "",
                "query": {
                    "geosearch": [{
                        "pageid": 38724,
                        "ns": 0,
                        "title": "Palais de l'Élysée",
                        "lat": 48.8701444,
                        "lon": 2.3164861,
                        "dist": 36,
                        "primary": ""
                    }, {
                        "pageid": 7161912,
                        "ns": 0,
                        "title": "Ambassade de Colombie en France",
                        "lat": 48.870139,
                        "lon": 2.317694,
                        "dist": 75.3,
                        "primary": ""
                    }, {
                        "pageid": 722651,
                        "ns": 0,
                        "title": "Place Beauvau",
                        "lat": 48.871081,
                        "lon": 2.316236,
                        "dist": 83.1,
                        "primary": ""
                    }, {
                        "pageid": 3652124,
                        "ns": 0,
                        "title": "Rue de Duras",
                        "lat": 48.870878,
                        "lon": 2.317868,
                        "dist": 96.4,
                        "primary": ""
                    }]
                }
            }
   
    # patching for place api    
    monkeypatch.setattr(
        'app.modules.api_manager.requests.get', 
        MockRequestsGetPlace
    ) 
    search_obj = api_manager.ApiManager("Elysée")
    search_obj.place_finder()
    # patching for wiki api
    monkeypatch.setattr(
        'app.modules.api_manager.requests.get',
        MockRequestsGetWiki
    )
    search_obj.articles_nearby()

    assert search_obj.articles_id == [
        38724,
        7161912,
        722651,
        3652124
    ]    


            #########################
            #                       #
            #  ===>  A FAIRE  <===  #
            #                       #
            #########################