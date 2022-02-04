#!/usr/bin/python3
import random

load = 1
while load == 1:
    print("Welcome to MAstermind")
    print("Choose the difficulty of the game 1=Easy, 2=Hard, 3=Nightmare")
    difficulty = int(input("Write the number of difficulty: "))
    if difficulty == 1:
        digitNumber = 3
    elif difficulty == 2:
        digitNumber = 4
    elif difficulty == 3:
        digitNumber = 5

    digits = ('0', '1', '3', '4', '5', '6', '7', '8', '9')
    code = ''

    # Part1: The machine selects their combination of number
    for i in range(digitNumber):
        chooseDigits = random.choice(digits)
        # in case the number repeats
        while chooseDigits in code:
            chooseDigits = random.choice(digits)
        code = code + chooseDigits

    # Part2: user start to play
    print("Start to guess one digit color of", digitNumber,
          "different digits colors")
    print("Combinations of colors: [[0 is white]; [1 is red]; [2 is orange]; \
[3 is blue]; [4 is yellow]; [5 is magenta]; [6 is black]; [7 is purple]; \
[8 is pink]; [9 is skyblue]]")
    proposal = input("Write your [code of colors] \
or [exit] if you want to finish: ")
    if (proposal == "exit"):
        exit()
    tryNumber = 1
    while proposal != code:
        tryNumber += 1
        hits = 0
        coincidences = 0
        for i in range(digitNumber):
            if proposal[i] == code[i]:
                hits += 1
                print("---> You    have a hit with the number", proposal[i],
                      "in the position ", i, ";)")
            elif proposal[i] in code:
                coincidences += 1
                print("---> You are near! You have a coincidence \
with the number", proposal[i], " try a new position")
        print("[Final] Your proposal(", proposal, ") \
have ", hits, " hits and ", coincidences, " \
coincidences")
        proposal = input(" Try another [code] or [exit] if you want to quit: ")
        if (proposal == "exit"):
            exit()

    print("[Congratulations] You win in", tryNumber, " tries")
    load = int(input("Do you want to continue playing? <1=yes, 0=no>: "))
