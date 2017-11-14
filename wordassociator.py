from random import *
from time import *

class wordclass:
    def __init__(self,word):
        self.word = word
        self.precedelist = []

    def precedes(self,word):
        self.precedelist.append(word)

    def printme(self):
        print "*-*"
        print self.word
        for word in self.precedelist:
            print word

class wordweb:
    def __init__(self):
        try:
            self.web = []
            filein = open("CombinedIn.txt","r")
            inputtext = filein.read()
            filein.close()
            self.parse(inputtext)
        except:
            print("something went wrong")

    def parse(self,sentence):
        """
        does all the work
        """
        words = sentence.split()
        for i in range(len(words)-1):
            dupe = self.checkfordupes(words[i])
            if dupe == -1:
                self.web.append(wordclass(words[i]))
                index = len(self.web)-1
                self.web[index].precedelist.append(words[i+1])
            else:
                self.web[dupe].precedelist.append(words[i+1])

    def checkfordupes(self, checkword):
        """
        returns position of duplicate, or -1 if no duplicate
        """
        for wordobject in self.web:
            if wordobject.word == checkword:
                return self.web.index(wordobject)
        return -1

    def recite(self):
        """
        So far, this function is sort of the top-level response generator.
        It gets the first word, then gets "next words" until we get to a "."
        """

        #This part chooses a capitalized first word
        firstwordisnotchosenyet = True
        while firstwordisnotchosenyet:
            start = randint(0,len(self.web)-1)
            startword = self.web[start].word
            if startword[0].isupper():
                firstwordisnotchosenyet = False

        #This part gets the next words until a "." is found
        next = self.web[start].word
        response = next
        lastletter = response[len(response)-1]
        while lastletter not in ".!?":
            next = self.nextword(next)
            response = response + " " + next
            lastletter = response[len(response)-1:]
        print response

    def nextword(self,currentword):
        currentindex = self.checkfordupes(currentword)
        numchoices = len(self.web[currentindex].precedelist)
        rand = randint(0,numchoices-1)
        return self.web[currentindex].precedelist[rand]

    def savewordweb(self):
        fileout = open("testfileout.txt","w")
        for word in self.web:
            for precedes in word.precedelist:
                fileout.write("".join([word.word," ",precedes,"\n"]))
        fileout.close()
        
        

def main():
    web = wordweb()
    inputloop = True
    while inputloop == True:
        sentence = raw_input()
        web.parse(sentence)
        inputloop = False

    for a in range(10):
        web.recite()
        raw_input()

##    web.savewordweb()

##    for word in web.web:
##        word.printme()

main()
