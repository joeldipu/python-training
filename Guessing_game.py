# Libraries needed for program.
import random
import time
# Creates chance parameters needed for end of program.
RESURRECTION_CHANCE = str(random.randint(0,4))
passing = "false"
# Program starts, this part creates all other parameters needed.
while 1 == 1:
    TRINUM = (20)
    THINKING_NUMBER = random.randint(1, 99)
    print("I have gotten a number between 1 and 99.")
    TRINUM_OPERATER = input("How many tries would you like?: ")

# Uses TRINUM_OPERATER to change the function TRINUM
    if TRINUM_OPERATER == "":
        pass
    else:
        TRINUM = int(TRINUM_OPERATER)
        TRINUM = TRINUM - 1
# Asks first guess
    guess = int(input("Guess the number: "))
# Checks the guess and
    for i in range(int(TRINUM)):
        if guess > THINKING_NUMBER:
            print("Sorry,too high")
            time.sleep(.5)
            guess = int(input("Guess it again: "))
            time.sleep(.75)
        elif guess < THINKING_NUMBER :
            print("Sorry,too low")
            time.sleep(0.5)
            guess = int(input("Guess it again: "))
            time.sleep(.75)
        elif guess == THINKING_NUMBER:
            print("Good job! It was " + str(THINKING_NUMBER) + "! ")
            passing = "true"

    if passing != "true":
    # Sad ending statement and chance for resurrection
        print("Sorry, you ran out of tries")
        print("")
        time.sleep(5)

    if passing != "true" and RESURRECTION_CHANCE == 2:
        print("You have been ressurected!")
        print("")
    else:
        print("you died")
        time.sleep(1000000)
