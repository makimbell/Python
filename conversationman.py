from random import *
from time import *

class bot:
    def __init__(self):
        '''
        initializes promptlist and responselist
        '''
        try:
            filename = open("responselist.lol",'r')
            lines = filename.readlines()
            filename.close()

            self.promptlist = []
            self.responselist = []
            self.activelist = []
            mode = "prompt"
            
            for linenum in range(len(lines)-1):
                if lines[linenum] == "***\n":
                    mode = "response"
                elif lines[linenum] == ">>>\n":
                    mode = "active"
                elif mode == "prompt":
                    self.promptlist.append(lines[linenum].strip("\n"))
                elif mode == "response":
                    self.responselist.append(lines[linenum].strip("\n"))
                elif mode == "active":
                    self.activelist.append(lines[linenum].strip("\n"))
        except:
            self.promptlist = ["hello"]
            self.responselist = ["hello"]
            self.activelist = ["what's your favorite color?", "what's your favorite number?", "what's your favorite shape?"]

        try:
            lines.index(">>>\n")
        except:
            self.activelist = ["what's your favorite color?", "what's your favorite number?", "what's your favorite shape?"]

##        print self.promptlist
##        print self.responselist
##        print self.activelist
        
    def respond(self, message):
        '''
        incorporates a delay based on the message length and
        displays message
        '''
        delaytime = 0.05*len(message)
        sleep(delaytime)
        print "\n" + message.upper() + "\n"

    def userin(self):
        '''
        returns user input
        '''
        return raw_input().lower().replace("  ", " ")

    def store(self, prompt, response):
        '''
        stores prompt and response in the promplist and responselist
        for later use
        '''
        self.promptlist.append(prompt)
        self.responselist.append(response)  

    def search(self, prompt):
        '''
        searches promptlist for prompt.  if it is found, then it returns
        the corresponding response
        '''
        lowest = self.promptlist.index(prompt)
        highest = lowest
##        print "possibilities:"
##        print "=============="
        while self.promptlist[lowest] == self.promptlist[highest]:
##            print self.responselist[highest]
            highest = highest + 1
##        print "=============="
        responseindex = randint(lowest,highest-1)
        return self.responselist[responseindex]
    
    def unknown(self, prompt):
        '''
        repeats what the user said last
        '''
        return "I don't know. " + prompt

    def newtopic(self):
        '''
        chooses one of the prompts stored in promptlist and returns it
        '''
##        print "**Topic not recognized.  Choosing new topic.**"
        if len(self.activelist) > 5:
            index = randint(len(self.activelist)-5,len(self.activelist)-2)
        else:
            index = randint(0,len(self.activelist)-2)
        return self.activelist.pop(index)

    def refreshactives(self):
        '''
        if activelist is less than 5, it will add random KNOWN promps to it
        '''
        while len(self.activelist) < 5:
            index = randint(0,len(self.promptlist)-1)
            self.activelist.append(self.promptlist[index])
##            print self.promptlist[index] + " was added to activelist"

    def sortlists(self):
        '''
        sorts promptlist and responselist alphabetically according to promptlist
        '''
        i = 0
        while i < len(self.promptlist)-1:
            if self.promptlist[i] > self.promptlist[i+1]:
                self.promptlist[i],self.promptlist[i+1] = self.promptlist[i+1],self.promptlist[i]
                self.responselist[i],self.responselist[i+1] = self.responselist[i+1],self.responselist[i]
                i = 0
            else:
                i = i + 1

    
def main():
    computer = bot()
    message = ""
    computer.respond("Hi, I'm Conversation Man.  Say whatever you want.")
    user = computer.userin()
    
    while True:
        computer.refreshactives()
        computer.sortlists()
        try:
            message = computer.search(user)
##            # User input was found"
        except:
##            # User input was not found"
            computer.activelist.append(user)
##            # User input was added to activelist"
            message = computer.newtopic()
##            # New topic has been selected and removed from activelist"
        computer.respond(message)
        user = computer.userin()
        
        if user == "bye":
            filename = open("responselist.lol",'w')
            for element in computer.promptlist:
                filename.write(element + "\n")
            filename.write("***\n")
            for element in computer.responselist:
                filename.write(element + "\n")
            filename.write(">>>\n")
            for element in computer.activelist:
                filename.write(element + "\n")
            filename.close()
            exit()

        computer.store(message,user)
##        # Loop has completed"
        
        
main()
