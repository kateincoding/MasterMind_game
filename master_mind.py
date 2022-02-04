#!/usr/bin/python3
"""Master Mind game"""
import random
from colorama import Fore,  Style
from art import *


if __name__ == "__main__":
    colors = ["green", "red", "blue", "yellow", "magenta",
              "black", "white", "cyan"]
    colora = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA,
              Fore.BLACK, Fore.WHITE, Fore.CYAN]
    keys = ["1", "2", "3", "4", "5", "6", "7", "8"]
    dict_val = dict(zip(keys, colors))
    dict_colors = dict(zip(colors, colora))
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
    switcher = {"1": 4, "2": 6, "3": 8}
    balls = switcher[str(difficult)]
    secret_list = random.sample(colors, k=balls)
    print("*****Please choose {} colors bettwen: *****\n".format(balls))
    art_2 = art("happy")
    print("                        {}\n".format(art_2))
    flag = 0
    for k in range(0, 8):
        n = 1;
        for color in colors:
            a = dict_colors.get(color)
            print(a, end="")
            if flag == 1:
                print(", ", end="")
            print("{}: {}".format(n, dict_val[str(n)] ), end="")
            flag = 1
            n += 1
            print(Style.RESET_ALL, end="")
        print()
        try:
            gamer_list = []
            for i in range(0, balls):
                a = str(input(">>>  "))
                if a not in keys:
                    raise Exception("Try again ...")
                gamer_list.append(a)
        except Exception:
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
            art_2 = dict_faces["{}".format(k)]
            print("try again ... {}".format(art_2))
            continue
        print(gamer_list)
        i = 0
        for color in gamer_list:
            if dict_val[color] == secret_list[i]:
                print(Fore.RED, end="")
                # Return ASCII text (default font) and
                # default chr_ignore=True
                Art = text2art("X")
                print(Art, end="")
                print(Style.RESET_ALL, end="")
            elif dict_val[color] in secret_list:
                print(Fore.WHITE, end="")
                Art = text2art("X")
                print(Art, end="")
            elif dict_val[color] not in secret_list:
                Art = text2art("0")
                print(Art, end="")
            i += 1
    print()
    art_2=art("sad and crying")
    print("                        {}".format(art_2))
    Art = text2art("Game Over")
    print(Art, end="")
