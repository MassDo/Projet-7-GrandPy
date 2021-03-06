
import re

from .stopwords import stw


class Parser():
    """
        This class instatiate object, that can pop out
        words from a sentence, if they are not meaningfull.
        This is done with pop() and the final sentence parsed 
        is in the text attribut.

        workflow:

            parser_obj = Paser("your sentence to parse")
            parser_obj.tokenized() ==> str sentence to list of words
            parser_obj.pop() ==> pop out words not meaningfull
            parser_obj.text ==> returned sentence parsed (str)
    """

    def __init__(self, raw_text=str()):
        """
            constructor

            param:
                raw_text: str of the user raw sentence.

            att: 
                text: return a str of the sentence parsed
        """
        self.raw_text = raw_text.lower()
        self.text = raw_text.lower()
        self.tokens = [] 

    def tokenized(self):
        """
           Tokenize str self.raw_text in a list of words,
           without accents and punctuation
           "Hello, world!" => ["Hello", "world"]
        """
        if self.raw_text != "":
            self.tokens = re.sub(r"[^\w]", " ", self.raw_text).split()
        else:
            raise Exception ("Cannot parse a empty text")

    def pop(self):
        """
            pop out the french stop words
            from the tokens attribute 
            and implement the text attribut 
            with the final str
        """ 
  
        #StopWords(sw) set
        sw = set()
        # ADD openclassrooms(oc) SW        
        sw.update(stw)
        # Make a temp list of tokens without stop words
        tokens_pop_sw = [w for w in self.tokens if not w in list(sw)]
        # Make a str from this list
        self.text = " ".join(tokens_pop_sw)