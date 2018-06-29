# imports
from random import randint

# FUNCTIONS

def randomCharacter(characters):
    lenChars = len(characters)
    rand = randint(0, lenChars - 1)
    return characters[rand]

def insertAtRandom(string, toInsert):
    lenString = len(string)
    rand = randint(0, lenString)
    result = ""

    for i in range(rand):
        result += string[i]

    result += toInsert
    for i in range(rand, lenString):
        result += string[i]

    # return
    return  result


def generatePassword(length):
    password = ""

    # add random amount of letters and numbers to the password
    for i in range(length):
        rand = randint(0, length)

        if rand % 2 == 0:
            password += randomCharacter("abcdefghijklmnopqrstuvwxyz")

        else:
            randomDigit = randomCharacter("0123456789")
            password = insertAtRandom(password, randomDigit)

    # return
    return password

# main fuction
def main():
    passwordLength = int(input("Password Length:"))
    numPasswords = int(input("How many passwords to generate?"))

    for i in range(numPasswords):
        print(generatePassword(passwordLength))


# RUN THE CODE
main()