def main():
    words = raw_input("Words: ")
    spellcheck(words)
    raw_input("Press enter to close")

def spellcheck(text):
    dictionary = open("DictionaryE.txt","r")
    dictionarywords = dictionary.readlines()
    dictionary.close()
    wordlist = text.split()

    misspelled = 0
    
    for word in wordlist:
        good = False
        word = word.strip('\n.,;/!@#$%^&*(){}[]:"<>?')
        word = word.lower()
        for correct in dictionarywords:
            if word +"\n" == correct:
                good = True
                break
        if good == False:
            print word,
            misspelled += 1

    if misspelled == 1:
        print " is misspelled."
    elif misspelled > 1:
        print " are misspelled."
    else:
        print "No misspelled words found."
    
main()

