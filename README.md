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


    print("[Congratulations] You win in", tryNumber, " tries")
    load = int(input("Do you want to continue playing? <1=yes, 0=no>: "))
```

### User(s) flow to play :video_game:
***
The idea of the game is for one player (the code-breaker) to guess the secret code chosen by the other player (the code-maker). The code is a sequence of 4 colored pegs chosen from six colors available. The code-breaker makes a serie of pattern guesses - after each guess the code-maker gives feedback in the form of 2 numbers, the number of pegs that are of the right color and in the correct position, and the number of pegs that are of the correct color but not in the correct position - these numbers are usually represented by small black and white pegs.

### Piece of code related to the algorithm or flow
***
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
