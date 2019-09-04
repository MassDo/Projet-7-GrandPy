"""
    Tests of the module chatbot
"""
import pytest

from app.toolbox import chatbot

def test_Chatbot_exist():
    """
        Test if class Chatbot from 
        chatbot module is created.
    """
    assert hasattr(chatbot, "Chatbot")

def test_attributs_exists():
    """
        Test if attributs from the constructor 
        of the class Chatbot exists
    """
    test_object = chatbot.Chatbot()
    assert hasattr(test_object, "input")
    assert hasattr(test_object, "text")
    assert hasattr(test_object, "name")
    assert hasattr(test_object, "address")
    assert hasattr(test_object, "latitude")
    assert hasattr(test_object, "longitude")
    assert hasattr(test_object, "link")
    assert hasattr(test_object, "parsed") 
    assert hasattr(test_object, "text_parsed_list")
    assert hasattr(test_object, "proximity")

def test_answer_exist():
    """
        Test if the instance method answer exit
    """
    test_object = chatbot.Chatbot()
    assert hasattr(test_object, "answer")

# NEW
def test_chatbot_missing_argument_raise_err():
    """
        Test if exception is raised if missing argument    
    """
    bot = chatbot.Chatbot()

    with pytest.raises(TypeError):
        assert bot.answer()
# NEW
def test_chatbot_text_Attribut_values_for_empty_search():
    """
        Test if exception is raised if empty input string,
        and test ifthe return value for text attribut
        is the message that can be used to answer to the user.    
    """
    bot = chatbot.Chatbot()
    bot.answer("")

    with pytest.raises(Exception):
        assert bot.text is "Désolé mon ptit j'ai la mémoire qui flanche,\
 je n'ai pas d'histoires sur cet endroit..."
# NEW
def test_chatbot_address_Attribut_value_for_empty_search_is_none():
    """
        Test if exception is raised if empty input string
        and if the attribute bot.address is none, in this case
        the front script will not create a response into 
        the chat buble to give the address.    
    """
    bot = chatbot.Chatbot()
    bot.answer("")

    with pytest.raises(Exception):
        assert bot.address is None
# NEW
def test_chatbot_name_Attribut_value_for_empty_search_is_none():
    """
        Test if exception is raised if empty input string
        and if the attribute bot.name is none, in this case
        the front script will not create a response into 
        the chat buble to give the name of the place researched.    
    """
    bot = chatbot.Chatbot()
    bot.answer("")

    with pytest.raises(Exception):
        assert bot.name is None
# NEW
def test_chatbot_coordinates_Attribut_values_for_empty_search_is_0():
    """
        Test if chatbot attributes for the the coordinates values are (0, 0)
        in case of answer method with empty user input. In case of 
        (0, 0) returned coordinates, the front .js scripts will not diplay
        a google map.     
    """
    bot = chatbot.Chatbot()
    bot.answer("")

    assert bot.latitude == 0
    assert bot.longitude == 0
