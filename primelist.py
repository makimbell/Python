def main():
    filefile = open("primelist.txt",'w')
    number = input("Number: ")
    printme=""
    numberlist=""
    for i in range(number):
        yesorno = isprime(i)
        if yesorno:
            printme += "*"
            numberlist += str(i) + ", "
        else:
            printme += "."
    filefile.write(printme)
    filefile.close
    #print numberlist
    raw_input("List has been printed to primelist.txt")
    
def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

main()
