class Helper:
    ''' Print the correct answers
    '''

    def __init__(self):
        pass

    def cheat_sheet(self, word_listed):                     # For debugging or if a beginner
        cheat = str(raw_input("do you want a cheatsheet? (yes or any key): "))
        if cheat.lower() == "y" or cheat.lower() == "yes":
            print ("")
            print ("The correct answers are:")
            print (", ").join(word_listed)
            print("")
        else:
            print ("")
            print ("Ok. lets start the test")
            print("")
            print("")
