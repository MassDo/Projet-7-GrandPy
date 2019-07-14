from app.toolbox import parser


class Test_parser():

    def test_parser_exists(self):
        """
            test if the class exists
        """
        assert hasattr(parser, "Parser")
        
    # Tokenize method test
    def test_tokenized_exists(self):

        """
        test if method tokenized exist

        """
        assert hasattr(parser.Parser, "tokenized")

    def test_tokenized_return(self):
        """
            test the return of the method tokenized
            it must return a list of the sentence words

        """
        raw_text = "Hello, world ! How are you ?"
        my_text_analyser = parser.Parser(raw_text)
        my_text_analyser.tokenized()        

        assert my_text_analyser.tokens == [
                                            "Hello",
                                            "world",
                                            "How",
                                            "are",
                                            "you"
        ]

    def test_pop_exists(self):
        """
        test if method pop exist

        """
        assert hasattr(parser.Parser, "pop")

    def test_stop_words_off(self):
        """
            Pop out the french stop words
            from the tokens attribute liste.
        """
        raw_text = "Bonjour, ou est la tour Eiffel ?"
        my_text_analyser = parser.Parser(raw_text)
        my_text_analyser.tokenized()
        my_text_analyser.pop()

        assert my_text_analyser.text == "Bonjour tour Eiffel"


# package: app
#     package: toolbox
#         module: parser.py      
#         module: stop_words_oc
#             ma constante à importer: stopwords  
# package: tests
#     package: test_toolbox
#         module: test_parser 

#         # je fais: from app.toolbox import parser
#                             # j'ai ModuleNotFoundError: No module named 'stop_words_oc'

