import random
import PhoneticAlphabet
alphabet = PhoneticAlphabet.PhoneticAlphabet()
alf = alphabet.alf()


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

    def word(self):
        word = self.lines[random.randrange(0, 100000)].rstrip("\n")
        return word

    def wordList(self, word):
        print ("")
        word_list = []
        for letter in word:
            word_list.append(alf.get(letter))
        return word_list