"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    '''
    Machine that counts number of words in a file (file must contain only one word on each line), and provides a method to randomly select one of those words.
    
    Accepts path_to_file as a string.
    
    >>> wf = WordFinder('words.txt')
    235886 words read
    '''
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        raw = open(path_to_file, 'r')
        self.words_list = self.extract_words(raw)
        print(f'{len(self.words_list)} words read')
    
        
    def extract_words(self, raw):
        '''
        Turn file into a list to work with in python
        '''
        return [line.strip() for line in raw]
     

    
    def random(self):
        '''
        When called this method provides a random word from the text document that was read.
        '''
        return choice(self.words_list)
    
class SpecialWordFinder(WordFinder):
    '''
    Special class to handle documents with blank lines and comments
    '''
    def extract_words(self, raw):
        '''
        When called this method provides a list of words that ignore blank lines and comments
        '''
        return [line.strip() for line in raw if line.strip() and not line.startswith('#')]