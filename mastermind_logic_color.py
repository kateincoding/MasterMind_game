#!/usr/bin/python3
"""Mastermind game"""

from cstr import cstr
import random


colors = ('black', 'red', 'green', 'yellow', 'blue',
              'magenta', 'cyan', 'white')


def difficulty_message(difficulty):
    if difficulty == 0:
        message = "Allowed colors:\n"
        for col in colors:
            ball = cstr('●').color(col)
            message += "{}: {}\n".format(col, ball)
    elif difficulty == 1:
        message = "Allowed colors:\n"
        for col in colors:
            ball = cstr('●').color(col)
            bright_ball = cstr('●').bright(col)
            message += "{}: {}\n".format(col, ball)
            message += "bright_{}: {}\n".format(col, bright_ball)
    elif difficulty == 2:
        message = "You can work with numbers (from 0 to 255) or colors.\n\
        Good luck. You need it.\n"
        message += "Allowed colors:\n"
        for col in colors:
            ball = cstr('●').color(col)
            bright_ball = cstr('●').bright(col)
            message += "{}: {}\n".format(col, ball)
            message += "bright_{}: {}\n".format(col, bright_ball)
    return message


def difficulty_array(difficulty):
    arr = []
    if difficulty == 0:
        for i in range(5):
            ball = cstr('●').color(random.choice(colors))
            arr.append(ball)
    elif difficulty == 1:
        for i in range(5):
            rdmnum = random.choice(range(0, 2))
            if rdmnum == 0:
                ball = cstr('●').color(random.choice(colors))
            else:
                ball = cstr('●').bright(random.choice(colors))
            arr.append(ball)
    elif difficulty == 2:
        for i in range(5):
            ball = cstr('●').color(random.choice(range(0, 256)))
            arr.append(ball)
    return arr


if __name__ == '__main__':
    gameover = 0
    difficulty = {'0': 'Easy', '1': 'Hard', '2': 'Mastermind'}

    while (gameover == 0):
        print("Welcome to Mastermind!")
        mode = input("""Select the game difficulty:
        0 = Easy
        1 = Hard
        2 = Mastermind
        Notes:
        - You have to choose 5 balls
        - Easy and Hard use words, Mastermind uses numbers
        - The combination can have two or more balls of the same color
        """)
        print("You choose {}".format(difficulty[mode]))
        print(difficulty_message(int(mode)))
        attempts = int(input("How many attempts do you want to try? "))
        print("""Remember: In the number match output, the numbers mean the following:
        0: No matches
        1: Match in color
        2: Match in color and position""")
        array = difficulty_array(int(mode))
        win = 0
        for i in range(1, attempts + 1):
            print("Attempt {} of {}".format(i, attempts))
            balls = []
            for j in range(1, 6):
                col = input("Color of the ball {} is ".format(j))
                try:
                    colint = int(col)
                    balls.append(cstr('●').color(colint))
                except ValueError:
                    if col[:7] == "bright_":
                        balls.append(cstr('●').bright(col[7:]))
                    else:
                        balls.append(cstr('●').color(col))
            matches = ""
            for b in range(len(array)):
                if balls[b] == array[b]:
                    matches += "2"
                elif balls[b] in array:
                    matches += "1"
                else:
                    matches += "0"
            print("Your matches: {}".format(matches))
            if matches == "22222":
                win = 1
                break
        print("The balls were:")
        for ball in array:
            print(ball + " ", end="")
        print()
        if win == 0:
            print("You lose!")
        else:
            print("Congratulations! You won!")
        if input("Do you want to play another party? y|n ") == "y":
            win = 0
        else:
            gameover = 1
