class StatsHolder:
    ''' holds the information for the program
    '''
    def __init__(self):
        self.total = 0
        self.total_correct = 0
        pass

    def results(self):
        print("")
        print ("you got " + str(self.total_correct) + " points" + " out of " + str(self.total))
        print("Correct answers: {:.2%} ".format(self.floatCorrectPercentage()))

    def floatCorrectPercentage(self):
        return self.total_correct / float(self.total)

