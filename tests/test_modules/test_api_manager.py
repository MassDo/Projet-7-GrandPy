from app.modules import api_manager


class Test_api_manager:


    def test_ApiManager_exist(self):
        """
            Test if class is created.
        """
        assert hasattr(api_manager, "ApiManager")

    def test_attributs_exist(self):
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

    def test_place_finder_exist(self):
        """
            Test if the instance method place_finder exit
        """
        test_object = api_manager.ApiManager("user parsed text")
        assert hasattr(test_object, "place_finder")
    
    def test_methode_place_finder(monkeypatch):  
        """ 
            The method place_finder must implement the instances attributs
            from the instance attribut parsed_text and the google place API:

                => name
                => address
                => latitude
                => longitude            

        """           
        class MockRequestsGet:
        
            def __init__(self, url, param=None):
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
        monkeypatch.setattr('requests.get', MockRequestsGet)

        # test de la fonction
        search_obj = api_manager.ApiManager("Elysée")
        search_obj.place_finder()

        assert search_obj.name == "Le Palais de L'Élysée"
        assert search_obj.address == "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France"
        assert search_obj.latitude == 48.8704156
        assert search_obj.longitude == 2.3167539




#########################
#                       #
#  ===>  A FAIRE  <===  #
#                       #
#########################

# https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mercedes usine&locationbias=ipbias&fields=formatted_address,name,geometry/location&inputtype=textquery&key=AIzaSyAVJ9UzNh0XIXQ3oT400XvlieLNsfY_2fk