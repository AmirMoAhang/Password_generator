import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')

class PasswordGenerator(ABC):
    """Abstract class to be a template to implement project
    """
    
    @abstractmethod
    def generate(self):
        pass
    

class PinGenerator(PasswordGenerator):
    """PIN password generator class
    """
    
    def __init__(self, length:int = 8):
        self.pin_length = length
    
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range (self.pin_length)])


class RandomPasswordGenerator(PasswordGenerator):
    """Generate random character base password
    """
    
    def __init__(self, length:int = 8, is_num:bool = False, is_symbol:bool = False):
        self.length = length
        self.is_num = is_num
        self.is_symbol = is_symbol
        self.characters = string.ascii_letters
        if is_num:
            self.characters += string.digits
        if is_symbol:
            self.characters += string.punctuation
        
    
    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range (self.length)])
        

class MemorablePasswordGenerator(PasswordGenerator):
    """Generate password that can be remember base on meaning full words"""
    
    def __init__(self, num_of_words:int = 5,
                 separator:str = '-',
                 cap:bool = False
        ):
        self.num_of_words = num_of_words
        self.separator = separator
        self.cap = cap
        
        
    def generate(self):
        words = nltk.corpus.words.words()
        pass_words = [random.choice(words) for _ in range(self.num_of_words)]
        if self.cap:
            pass_words = [word.capitalize() for word in pass_words]
        return self.separator.join(pass_words)
   