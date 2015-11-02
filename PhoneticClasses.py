import random
class CreateWordList:

    def __init__(self, ):
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