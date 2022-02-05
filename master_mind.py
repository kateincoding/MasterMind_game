#!/usr/bin/python3
"""Master Mind game"""
import random
from colorama import Fore,  Style
from balls import Balls
from art import *

dict_faces = {
    "0": art("kissing"),
    "1": art("happy hug"),
    "2": art("meow"),
    "3": art("worried"),
    "4": art("confused7"),
    "5": art("crazy"),
    "6": art("angry1"),
    "7": art("exorcism")
 }
colors = ["green", "red", "blue", "yellow", "magenta", "cyan"]
colora = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA,
          Fore.CYAN]
keys = ["1", "2", "3", "4", "5", "6"]
dict_val = dict(zip(keys, colors))
dict_colors = dict(zip(colors, colora))
dict_keys = dict(zip(colors, keys))

def mastermind():
    while (True):
        art_2 = art("happy")
        try:
            print("*****Please choose the level of difficulty: *****")
            Art = text2art("123", font='block', chr_ignore=True)
            print(Art)
            difficult = int(input(">>> "))
            if difficult not in [1, 2, 3]:
                print("*****Please choose a valid option {}*****".format(art_2))
                continue
            break
        except Exception:
            print("*****Please choose a valid option {}*****".format(art_2))
            continue
    switcher = {"1": 4, "2": 5, "3": 6}
    balls = switcher[str(difficult)]
    secret_list = random.sample(colors, k=balls)
    print(secret_list)
    color_fak =  ["white" for i in range(len(secret_list))]
    balls_t =  Balls()
    balls_t.draw_aptems(color_fak, -400, 340)
    balls_t.draw_separator()
    coor = -380
    for k in range(0, 8):
        print("*****Please choose {} colors bettwen: *****\n".format(balls))
        art_2 = art("happy")
        print("                        {}\n".format(art_2))
        to_list = list(dict(enumerate(colors)).keys())
        to_list = list(map(lambda x: x + 1, to_list))
        print_colors(colors, to_list)

        print()
        try:
            gamer_list = []
            for i in range(0, balls):
                a = str(input(">>>  "))
                if a not in keys:
                    raise Exception("Try again ...")
                gamer_list.append(a)
        except Exception:
            art_2 = dict_faces["{}".format(k)]
            print("try again ... {}".format(art_2))
            continue
        i = 0
        validate = []
        color_pin = []
        pin = []
        for color in gamer_list:
            if dict_val[color] == secret_list[i]:
                print(Fore.RED, end="")
                # Return ASCII text (default font) and
                # default chr_ignore=True
                Art = text2art("X")
                print(Art, end="")
                color_pin.append("red")
                pin.append("X")
                print(Style.RESET_ALL, end="")
            elif dict_val[color] in secret_list:
                print(Fore.WHITE, end="")
                Art = text2art("X")
                print(Art, end="")
                pin.append("X")
                color_pin.append("white")
                print(Style.RESET_ALL, end="")
            elif dict_val[color] not in secret_list:
                print(Fore.BLUE, end="")
                Art = text2art("0")
                print(Art, end="")
                pin.append("0")
                color_pin.append("blue")
            validate.append(dict_val[color])
            i += 1
        if secret_list == validate:
            Art = text2art("Congratulations...!")
            print(Art)
            ask()
        art_2 = dict_faces["{}".format(k)]
        print("***** You chose this *****")
        validate_keys = [dict_keys.get(x) for x in validate if dict_keys.get(x)]
        print_colors(validate, validate_keys)
        balls_t.draw_aptems(validate, -400, coor)
        balls_t.draw_pins(color_pin, 50, coor)
        print("try again ... {}".format(art_2))
        coor += 90

 
    art_2 = art("sad and crying")
    print("***** you finished all your chances {} *****".format(art_2))
    print("***** The correct answer was *****")
    secret_keys = [dict_keys.get(x) for x in secret_list if dict_keys.get(x)]
    print_colors(secret_list, secret_keys)
    balls_t.draw_aptems(secret_list, -400, 340)
    coor += 90
    print()
    ask()


def print_colors(list_color, list_gamer):
    """Function to print colors"""
    n = 0
    flag = 0
    for color in list_color:
        if flag == 1:
            print(", ", end="")
        print(dict_colors[list_color[n]], end="")
        print("{}: {}".format(list_gamer[n], list_color[n]), end="")
        flag = 1
        n += 1
        print(Style.RESET_ALL, end="")
    print()


def ask():
    art_2 = dict_faces["2"]
    print("Do you want play again ...? {}".format(art_2))
    answer = str(input(">>>  "))
    if answer == "yes":
        mastermind()
    elif answer == "no":
        art_2=art("sad and crying")
        print("                        {}".format(art_2))
        Art = text2art("Game Over")
        print(Art, end="")
        print("Thanks for play ...! {}".format(art_2))
        exit(0)
    print("           Invalid option          ")
    ask()


mastermind()
