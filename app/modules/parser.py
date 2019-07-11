import re

import nltk

class Parser():

    def __init__(self, raw_text=str()):
        """
            constructor

            param:
                raw_text: str of the user raw sentence.

            att: 
                text: return a str of the sentence parsed
        """
        self.raw_text = raw_text
        self.text = raw_text
        self.tokens = [] 

    def tokenized(self):
        """
           Tokenize str self.raw_text in a list of words,
           without accents and punctuation
           "Hello, world!" => ["Hello", "world"]
        """
        self.tokens = re.sub(r"[^\w]", " ",  self.raw_text).split()


    def pop(self):
        """
            pop out the french stop words
            from the tokens attribute 
            and implement the text attribut 
            with the final str
        """    
        sw = set()
        # Find st database
        sw = nltk.corpus.stopwords.words('french')         
        # Make a temp list of tokens without stop words
        tokens_pop_sw = [w for w in self.tokens if not w in list(sw)]
        # Make a str from this list
        self.text = " ".join(tokens_pop_sw)
        

