import random
import string

import nltk

def GeneratePinPassword(length:int = 8) -> str:
    """Generate PIN password

    Args:
        length (int, optional): length of password string. Defaults to 8.

    Returns:
        str: Generated password
    """
    return ''.join([random.choice(string.digits) for _ in range (length)])


def GenerateRandomPassword(length:int = 8, is_num:bool = False, is_symbol:bool = False) -> str:
    """Generate random password

    Args:
        length (int, optional): length of password string. Defaults to 8.
        is_num (bool, optional): contains digital number or not. Defaults to False.
        is_symbol (bool, optional): contains strings symbol or not. Defaults to False.

    Returns:
        str: Generated password
    """
    characters = string.ascii_letters
    if is_num:
        characters += string.digits
    if is_symbol:
        characters += string.punctuation
    
    return ''.join([random.choice(characters) for _ in range (length)])


def GenerateMemorablePassword(num_of_words:int = 4, seprator:str = '-', cap:bool = False) -> str:
    """Generate a password based on meaning full words

    Args:
        num_of_words (int, optional): number of words. Defaults to 4.
        seprator (str, optional): seprator between words. Defaults to '-'.
        cap (bool, optional): capitalize words or not. Defaults to False.

    Returns:
        str: Generated password
    """
    words = nltk.corpus.words.words()
    pass_words = [random.choice(words) for _ in range(num_of_words)]
    
    if cap:
        pass_words = [word.capitalize() for word in pass_words]

    return seprator.join(pass_words)









