#!/usr/bin/python2

import WordlistCreator
import Helper
import Spelling
import Stats


def main():
    random_word_fetcher = WordlistCreator.CreateWordList()
    random_word_fetcher.fileread("words.txt")
    helper = Helper.Helper()
    spelling = Spelling.Spelling()
    print("")
    print("")
    print ("welcome to phonetic spelling test!")
    print("")
    print("")
    done = False
    while not done:
        print ("")

        word = random_word_fetcher.word()
        word_listed = random_word_fetcher.wordList(word)
        helper.cheatSheet(word_listed)
        result = Stats.StatsHolder()
        print ("use the phonetic alphabet to spell the word:")
        print word
        spelling.questions(word, result)
        
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
