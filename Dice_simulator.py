import random

def checkerror(number):

    if number.isnumeric():
        number = int(number)
        return number
    else:
        print("Sorry! You must have a integer as your number of sides")
        exit(1)

print("Welcome to the dice simulator?")

NUM_SIDES = input ("How many sides would you like on your dice")
NUM_SIDES = checkerror(NUM_SIDES)

NUM = input ("How many dice would you like?")
NUM_SIDES = checkerror(NUM)

ZIF = input ("Would you like zeroes?")


if NUM_SIDES == 0:
    NUM_SIDES == -1

if ZIF == "yes":
    ZNUM = 0

NUM = int(NUM)

def main():
    x = 1

    for i in range (NUM):
        print("dice #" + str(x) + " " + "is" , str(random.randint(ZNUM, NUM_SIDES)))
        x = x + 1






if __name__ == "__main__":
    main()





















