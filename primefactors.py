def main():
    number = input("Number: ")
    findprimefactors(number)
##    for i in range(number):
##        findprimefactors(i)
##        print("\n")
    raw_input("Press enter to close")

def findprimefactors(number):
    x = 2
    done = False
    while done==False:
        if x <= (number):
            if number % x == 0:
                print x,
                number = number / x
                x=2
            else:
                x = x+1
        else:
            done = True
main()
