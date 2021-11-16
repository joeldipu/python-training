# starting code and variables.
import time
import random

opponent_rcp_number = random.randint(1, 3)

if opponent_rcp_number == 1:
    opponent_rcp = "rock"

if opponent_rcp_number == 2:
    opponent_rcp = "paper"

if opponent_rcp_number == 3:
    opponent_rcp = "scissors"

# Welcome statement and rules
print("Welcome to the rock paper scissors CHAMPIONSHIPS!")
print()
print()
# print() command creates new line. the past two statements just created two blank lines.
time.sleep(2)
# time.sleep command creates pause in terminal. time.sleep(2) means to wait two seconds
print("The rules are simple: say rock, paper, or scissors.")
print()
time.sleep(1.9)
print('Paper "beats" rock. This means that if you play paper, and you opponent plays rock, you win.')
print()
time.sleep(2.69)
print("Scissors beats paper, so if you opponent plays scissors, you lose.")
print()
time.sleep(1.9)
print("If your opponent plays the same thing as you, you go again.")
print()
time.sleep(2)
print("The 'wins' are shown here:")
print()
time.sleep(2)
print("rock beats scissors ")
time.sleep(1.7)
print("scissors beats paper")
time.sleep(1.7)
print("paper beats rock")
time.sleep(1.7)
print()
print("Now let's start!")
print()
print()


# end of code for the rules.
# creates rps
def game():
    rps = input("rps: ")
    # r-p loss
    if (rps == "rock" or rps == "Rock") and (opponent_rcp == "paper" or opponent_rcp == "Paper":
        print("you lose")
        print("Computer had " + opponent_rcp)
        game()
    # p-s loss
    elif rps == "paper" and opponent_rcp == "scissors" or rps == "Paper" and opponent_rcp == "scissors":
        print("you lose")
        game()
    # s-r loss
    elif rps == "scissors" and opponent_rcp == "rock" or rps == "Scissors" and opponent_rcp == "rock":
        print("you lose")
        game()
    # r-r tie
    elif (rps == "rock" and opponent_rcp == "rock") or (rps == "Rock" and opponent_rcp == "rock"):
        print("you tied")
        game()
    # s-s tie
    elif rps == "scissors" and opponent_rcp == "scissors" or rps == "Scissors" and opponent_rcp == "scissors":
        print("you tied")
        game()
    # p-p tie
    elif rps == "paper" and opponent_rcp == "paper" or rps == "Paper" and opponent_rcp == "paper":
        print("you tied")
        game()
    # r-s win
    elif rps == "rock" and opponent_rcp == "scissors" or rps == "Rock" and opponent_rcp == "scissors":
        print("you won!")

        game()
    # p-r win
    elif rps == "paper" and opponent_rcp == "rock" or rps == "Paper" and opponent_rcp == "rock":
        print("you won!")
        #points = points + 1
        game()


game()
