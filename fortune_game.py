key_status = "unlocked"
print("FORTUNE GAME")

print ("Options" , "To switch, type enter")


def start():
    global op1
    op1 = input("to spin the wheel, type 1: ")
    op2 = input("for setings, type 2: ")

    if key_status == "unlocked":
        op3 = input("to redeem, type 3")

start()

if op1 == "1":
    check = input("Are you SURE you want to spin the wheel?")

if check == ("yes"):
    pass
elif check == ("no")


