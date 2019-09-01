"""
    Tests of the module chatbot
"""
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
