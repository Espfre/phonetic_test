#!/usr/bin/python2

import random

alf = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
       'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
       'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x':
       'x-ray', 'y': 'yankee', 'z': 'zulu'}

'''
                 imports and global variables above this line
                 Functions under this line
'''


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


def word_list(word):                            # Makes a list of the chosen word
    print ("")
    word_list = []
    for letter in word:
        word_list.append(alf.get(letter))
    return word_list    
    
    
def answer(word, word_listed):
                           # Lets the user input answer and checks if its correct
                           # while keeping a running total of the mistakes
    print ("")
#   answer = []            # debugging
    total_mistakes = 0
    for i in word:
        print ("")
        print ("The character to spell is: " + i)
        print("")
        answer_current = (raw_input("spell the character using the phonetic alphabet: ").lower())
#       answer.append(answer_current)
        trans = alf.get(i)

        if answer_current == trans:
            print("")
            print ("Correct")
        else:
            print("")
            print ("wrong")
            print ("The correct answer is: " + trans)
            total_mistakes += 1
        print("")
    print ("you got a total of, " + str(total_mistakes) + " answers wrong")
    
    return answer


def cheatsheet(word_listed):                     # For debugging or if a beginner
    cheat = str(raw_input("do you want a cheatsheet? (yes or any key): "))
    if cheat.lower() == "y" or cheat.lower() == "yes":
        print ("")
        print word_listed
        print("")
    else:
        print ("")
        print ("Ok. lets start the test")
        print("")
        print("") 

'''
             Main loop under under this line
'''


def main():
    word_object = CreateWordList()
    word_object.fileread("words.txt")
    print("")
    print("")
    print ("welcome to phonetic spelling test!")
    print("")
    print("")
    done = False
    while not done:
        print ("")

        word = word_object.word()
        word_listed = word_list(word)
        cheatsheet(word_listed)
        print word
        answer(word, word_listed)
        
        for i in range(10):
            quit = str(raw_input("do you want another word to spell? : "))
            if quit.lower() == "no" or quit.lower() == "n":
                print ("")
                print ("Bye")
                print ("")
                done = True
                break
                
            elif quit.lower() == "yes" or quit.lower() == "y":
                break
            
            else:
                print ("you have to type either yes, y, no or n. please answer again")
                done = True
    

if __name__ == "__main__":
    main()
