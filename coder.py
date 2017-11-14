from easygui import *
from random import *
from sys import *
import re

###############################################################################
###############################################################################
######## Decrypt start
###############################################################################
###############################################################################
'''
decrypt is the complicated one. It is basically a cryptoquip solver.
'''
def decrypt(ctext, dictionary):
    possibilities = getpossibilities(ctext, dictionary)
    """
    solving algorithm:
    A)Find word with the fewest possibilities
        If any word has 0 possibilities, undo the last assignment you made
    Choose the Nth word from it
    Assign letters learned from that word to the key
    Refresh possibilities
    Go back to A)
    """
    print possibilities
    return "not finished"

'''
leastpossibilities takes the possibilities list (of lists) and returns the
(first level) index of the word with the fewest possibilities
'''
def leastpossibilities(possibilities):
    output = 0
    for i in range(len(possibilities)):
        if len(possibilities[i]) == 0:
            return -1
        elif len(possibilities[i]) < len(possibilities[output]):
            output = i
    return output

'''
getpossibilities takes a sentence and returns a list of lists,
which contains the possible word matches for each word sent to it
'''
def getpossibilities(ctext, dictionary):
    '''
    First we find the words in the dictionary that are the same
    length as the first word we are trying to solve
    '''
    possibilities = []
    for i in range(len(ctext.split())): # For each word
        possibilities.append([])
        
    '''
    populate "possibilities" with the only possible words that can match
    '''
    wordindex = -1
    for cword in ctext.split():
        wordindex += 1
        for dicword in dictionary:
            if samelength(dicword.strip('\n'),cword) and abcformat(dicword.strip('\n')) == abcformat(cword):
                possibilities[wordindex].append(dicword)    
    return possibilities

def samelength(dicword, cword):
    return len(dicword.strip('\n')) == len(cword)

'''
abcformat takes a word and converts it to "abcformat" like this:
baby --> ABAC
cat ---> ABC
Food --> ABBC
'''
def abcformat(word): # make sure dicword is stripped.  cword doesn't have to be lowercase?
    formatletter = 'A'
    output = 'A'
    previousletters = word[0] # since we already "did" the first letter (output = 'A')
    for index in range(1,len(word)):
        if previousletters.find(word[index]) != -1: # if current letter IS a duplicate
            # add an amount to "A" that depends on how many unique
            # letters there are, and which one we're on
            output += chr(ord('A')+previousletters.find(word[index]))
        else:
            formatletter = chr(ord(formatletter)+1) # advances A to B, B to C, etc
            output += formatletter
            previousletters += word[index]
    return output

###############################################################################
###############################################################################
######## Decrypt Finish
###############################################################################
###############################################################################
        

'''
plusorminuschar shifts each character NUM positions in the ascii table
'''
def plusorminuschar(ctext, num):
    dwords = "" #this is the final output
    dword = "" #this is a single word.  this is cleared after each word
    for cword in ctext.split(): #splits up encoded text into words
        dword = ""
        for pos in range(len(cword)):
            cascii = ord(cword[pos])
            dascii = cascii + num
            if dascii > 127:
                dascii -= 95 # We want to deal with characters 32 to 127
            elif dascii < 32:
                dascii += 95
            dword += chr(dascii)
        dwords += dword + " "
    return dwords

'''
plusorminusword shifts each word NUM positions in the dictionary
'''
def plusorminusword(ctext, dictionary, num):
    dwords = ""
    for cword in ctext.split():
        index = -1
        for dicword in dictionary:
            index += 1
            if cword.lower().strip('!@#$%^&*()_+{}|:"<>?-=[]\;,./') == dicword.strip("\n"):
                dword = dictionary[index+num].strip("\n")
                break
            dword = cword.upper()
        dwords += dword + " "
    return dwords


'''
creates a user interface that allows the user to select encryption method
'''
def main():
    dictionaryfile = open("DictionaryE.txt")
    dictionary = dictionaryfile.readlines()
    dictionaryfile.close()
    choices = ["Character shift","Word shift","Cryptoquip solver"]
    while True:
        encodedtext = textbox("Enter the text you want to encode or decode")
        codetype = buttonbox("What do you want to do?",None,choices)
        if codetype == choices[0]:
            decodedtext = plusorminuschar(encodedtext, input("Shift by: "))
        elif codetype == choices[1]:
            decodedtext = plusorminusword(encodedtext, dictionary, input("Shift by: "))
        elif codetype == choices[2]:
            decodedtext = decrypt(encodedtext, dictionary)

        textbox("Here is the result: ", "", decodedtext)
        if not boolbox("Continue?"):
            exit()

'''
Main code goes here
'''
main()
