file1 = open("sentences.txt","r")
lines = file1.readlines()
file1.close()

file2 = open("sentences2.txt","w")

for line in lines:
    for letter in line:
        if letter.isupper():
            file2.write(letter.lower())
        else:
            file2.write(letter)
