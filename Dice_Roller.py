ZNUMOP = 1


import random

def checkerror(var):
    if var.isnumeric():
        pass
    else:
        print("Sorry, you need an integer as your number of dice/sides")
        exit(1)

print("DICE SUPEROLLER!")
NUM_SIDES = input("How many sides would you like on your dice?: ")
checkerror(NUM_SIDES)
NUM = input("How many dice would you like?: ")
checkerror(NUM)
ZNUM = input("Would you like zeroes? Please type Y or N")

if ZNUM == "N":
    pass
elif ZNUM == "Y":
    ZNUMOP = 0
    NUM_SIDES = NUM_SIDES - 1
else:
    print("Please type  Y or N for zeroes.")
    exit(-20000000000000-0000)



x = 1
for i in range(int(NUM)):
    print("dice #" + str(x) + " is " + str(random.randint(int(ZNUMOP), int(NUM_SIDES))))
    x = x + 1