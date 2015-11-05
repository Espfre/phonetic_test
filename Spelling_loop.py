alf = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
       'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
       'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x':
       'x-ray', 'y': 'yankee', 'z': 'zulu'}

'''
                 imports and global variables above this line
                 Functions under this line
'''


class Spelling:
    ''' Lets the user input answers and check if its correct
    '''

    def __init__(self):
        pass

    def questions(self, word, result):

        print ("")

        for i in word:
            print ("")
            print ("The character to spell is: " + i)
            print("")
            answer_current = (raw_input("spell the character using the phonetic alphabet: ").lower())
            trans = alf.get(i)
            result.total += 1

            if answer_current == trans:
                print("")
                print ("Correct")
                result.total_correct += 1
            else:
                print("")
                print ("wrong")
                print ("Your answer was:       " + answer_current)
                print ("The correct answer is: " + trans)
        print result.results()


