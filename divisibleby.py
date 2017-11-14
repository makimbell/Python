def main():
    filefile = open("divisibleby.txt",'w')
    number = input("Number: ")
    printme=""
    for i in range(number):
        if divisibleby(i) != 0:
            printme += str (i) + "\t" + str(divisibleby(i)) + "\n"
    filefile.write(printme)
    filefile.close
    #print numberlist
    raw_input("List has been printed to divisibleby.txt")
    
def divisibleby(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return x
    return 0

main()
