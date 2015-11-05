import random

alf = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
       'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
       'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x':
       'x-ray', 'y': 'yankee', 'z': 'zulu'}


class CreateWordList:
    ''' creates a dictionary of words from a file that it can pull random words from
    '''

    def __init__(self):
        self.lines = {}
        pass

    def fileread(self, filename):
        content = open(filename)
        self.lines = content.readlines()
        content.close()
        return self.lines

    def word(self):                                      # Gets a random word for the test
        word = self.lines[random.randrange(0, 10000)].rstrip("\n")
        return word

    def word_list(self, word):                            # Makes a list of the chosen word
        print ("")
        word_list = []
        for letter in word:
            word_list.append(alf.get(letter))
        return word_list