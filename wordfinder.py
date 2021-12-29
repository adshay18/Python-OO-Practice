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
        self.read_num_words()
    
        
    def read_num_words(self):
        '''
        Function called to read the total number of words in a file, granted the file only contains one word per line.
        '''
        count = 0
        txt_file = open(self.path_to_file)
        for line in txt_file:
            count += 1
        txt_file.close()
        print(f'{count} words read')

    
    def random(self):
        '''
        When called this method provides a random word from the text document that was read.
        '''
        words_list = []
        txt_file = open(self.path_to_file)
        for line in txt_file:
            words_list.append(line.strip())
        txt_file.close()
        return choice(words_list)