import random

randomnumber = random.randint(1, 5)

print("This is a quote writer")
author = input("Who would you like a quote from? (William Shakespear, Winston Churchill, Galileo Galilei) ")
numberquotes = input("How many quotes would you like? ")

if numberquotes.isalpha():
    print("Sorry, " + numberquotes + " is not an integer, please try again.")

elif author == "William Shakespear" or author == "william shakespear" or author == "William shakespear" or  author == "william Shakespear":
    numberquotes = int(numberquotes)

    for i in range(numberquotes):

        if randomnumber == 1:
            print("To be or not to be")

        if randomnumber == 2:
            print("No legacy is so rich as honesty")

        if randomnumber == 3:
            print("All that glitters is not gold")

        if randomnumber == 4:
            print("What a piece of work is a man")
        randomnumber = random.randint(1, 5)

elif author == "Winston churhill" or author == "winston Churchill" or author == "winston churchill" or author == "Winston Churchill":
    numberquotes = int(numberquotes)

    for i in range(numberquotes):
        if randomnumber == 1:
            print("If you're going through hell, keep going.")

        if randomnumber == 2:
            print("You have enemies? Good. That means you've stood up for something, sometime in your life")

        if randomnumber == 3:
            print("We make a living by what we get, but we make a life by what we give.")

        if randomnumber == 4:
            print("To improve is to change; to be perfect is to change often.")

        if randomnumber == 5:
            print("The price of greatness is responsibility.")

        randomnumber = random.randint(1, 5)


elif author == "Galileo Galilei" or author == "galileo Galilei" or author == "Galileo galilei" or author == "galileo galilei" or author == "galileo" or author == "Galileo":
    numberquotes = int(numberquotes)

    print(" ")

    for i in range(numberquotes):
        if randomnumber == 1:
            print("I have never met a man so ignorant that I couldn't learn something from him.")

        if randomnumber == 2:
            print("Measure what is measurable, and make measurable what is not so.")

        if randomnumber == 3:
            print("You cannot teach a man anything, you can only help him find it within himself.")

        if randomnumber == 4:
            print("The Bible shows the way to go to heaven, not the way the heavens go.")

        if randomnumber == 5:
            print("Where the senses fail us, reason must step in.")
        randomnumber = random.randint(1, 5)
else:
    print("Sorry, " + author.capitalize() + " is not a listed quote writer, please try again.")