# MasterMind_game :brain:
HackDay: Coding the game MasterMind 
Mastermind is a board game of ingenuity and reflection for two players. It is played on a board with small black and white tiles and other colors, of a somewhat larger size. One of the players chooses a number of colored tiles, 4 in the original game, and puts a secret code hidden from the other player

### Campus presentation 🎓
***
  [Holberton School](https://www.holbertonschool.com/) is a computer science school founded in Silicon Valley to address the gap in the education system for aspiring software engineers.
After Holberton School opened its doors in 2016, the world’s most innovative companies have noticed. Graduates have found jobs at LinkedIn, Google, Tesla, Docker, Apple, Dropbox, Facebook, Pinterest, Genentech, Cisco, IBM, and more.

### Presentation of the language 💻
***
####  Python
Python is a programming language that lets you work quickly and integrate systems more effectively. 

### Algorithm put in place

```sh
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
```

### User(s) flow to play :video_game:
***
The idea of the game is for one player (the code-breaker) to guess the secret code chosen by the other player (the code-maker). The code is a sequence of 4 colored pegs chosen from six colors available. The code-breaker makes a serie of pattern guesses - after each guess the code-maker gives feedback in the form of 2 numbers, the number of pegs that are of the right color and in the correct position, and the number of pegs that are of the correct color but not in the correct position - these numbers are usually represented by small black and white pegs.

### Piece of code related to the algorithm or flow
***
```sh
def mastermind():
    while (True):
        art_2 = art("happy")
        play_music("start.mp3")
        try:
            print("\n*****Please choose the level of difficulty: *****")
            Art = text2art("123", font='block', chr_ignore=True)
            print(Art)
            difficult = input(">>> ")
            if str(difficult) == "exit":
                play_music("game_over.mp3")
                sleep(4)
                exit(0)
            difficult = int(difficult)
            if difficult not in [1, 2, 3]:
                print("*****Please choose a valid option {}*****".format(art_2))
                continue
            break
        except Exception:
            print("*****Please choose a valid option {}*****".format(art_2))
            continue
    switcher = {"1": 4, "2": 5, "3": 6}
    balls = switcher[str(difficult)]
    # Creating secret list colours
    secret_list = random.sample(colors, k=balls)
    color_fak =  ["white" for i in range(len(secret_list))]
    balls_t =  Balls(difficult)
    balls_t.draw_aptems(color_fak, -400, 340)
    balls_t.draw_separator()
    coor = -380
    aptems = 8
    print("Now you have 8 chances to solve the puzzle {}".format(dict_faces.get("1")))
    sleep(1)
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
                if a == "exit":
                    play_music("game_over.mp3")
                    sleep(4)
                    exit(0)
                if a not in keys:
                    raise Exception("Try again ...")

                gamer_list.append(a)
        except Exception:
            art_2 = dict_faces["{}".format(k)]
            play_music("game_over.mp3")
            print("try again ... {}".format(art_2))
            aptems -= 1
            count_aptems(aptems)
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
            play_music("grats.mp3")
            Art = text2art("Congratulations...!")
            balls_t.draw_aptems(secret_list, -400, 340)
            sleep(4)
            print(Art)
            ask()
        art_2 = dict_faces["{}".format(k)]
        print("***** You chose this *****")
        validate_keys = [dict_keys.get(x) for x in validate if dict_keys.get(x)]
        print_colors(validate, validate_keys)
        balls_t.draw_aptems(validate, -400, coor)
        balls_t.draw_pins(color_pin, 50, coor)
        print("try again ... {}".format(art_2))
        play_music("game_over.mp3")
        aptems -= 1
        count_aptems(aptems)
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

```

### Screenshots of the game
***
The game has 3 lvls :
1. lvl 1 = 4 balls 
2. lvl 2 = 5 balls 
3. lvl 3 = 6 balls

<div align="center">
  <img src="https://imgur.com/59D84Yx.png" width=100%/>
  <img src="https://imgur.com/Vy2wRKM.png" width=100%/>
  <img src="https://imgur.com/2IIgVi2.png" width=100%/>
  <img src="https://imgur.com/KsOft8Z.png" width=100%/>
</div>

### And of course a GitHub link to your code
