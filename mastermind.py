#!/usr/bin/python3
import random

load = 1
while load == 1:
    print("Welcome to MAstermind")
    print("Choose the difficulty of the game 1=Easy, 2=Hard, 3=Difficult")
    difficulty = int(input("Write the number of difficulty: "))
    if difficulty == 1:
        digitNumber = 3
    elif difficulty == 2:
        digitNumber = 4
    elif difficulty == 3:
        digitNUmber = 5

    digits = ('0', '1', '3', '4', '5', '6', '7', '8', '9')
    code = ''

    for i in range(digitNumber):
        chooseDigits = random.choice(digits)
        # in case the number repeats
        while chooseDigits in code:
            chooseDigits = random.choice(digits)
        code = code + chooseDigits

    # Part2: user start to play
    print("Start to guess one digit of", digitNumber, "different digits")
    proposal = input("Write your number: ")
    tryNumber = 1
    while proposal != code:
        tryNumber += 1
        hits = 0
        coincidences = 0
        for i in range(digitNumber):
            if proposal[i] == code[i]:
                hits += 1
                print("---> You    have a hit with the number", proposal[i],"in the position ", i, ";)")
            elif proposal[i] in code:
                coincidences += 1
                print("---> You are near! You have a coincidence with the number", proposal[i], " try a new position")
        print("[Final] Your proposal(",proposal,") have ", hits, " hits and ", coincidences, " coincidences")
        proposal = input(" Try another code: ")

    print("[Congratulations] You win in", tryNumber, " tries")
    load = int(input("Do you want to continue playing? <1=yes, 0=no>: "))
