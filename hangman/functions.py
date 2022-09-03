import random

# HANGMAN FUNCTIONS
# 3. record (record user's total games, wins, and loses)

#images of the hangman

# randomly chooses word
def randomChoose():
    with open("input.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        secretWord = random.choice(words)
        #print(secretWord)

        startGame(secretWord)

# start the actual game after getting user input
def startGame(secretWord):
    print("game will start")
    hangMan = ["""
    ________
       |   |
           |
           |
           |
    _______|
    ""","""
    ________
       |   |
       O   |
           |
           |
    _______|
    ""","""
    ________
       |   |
       O   |
       |   |
           |
    _______|
    ""","""
    ________
       |   |
       O   |
       |\  |
           |
    _______|
    ""","""
    ________
       |   |
       O   |
      /|\  |
           |
    _______|
    ""","""
    ________
       |   |
       O   |
      /|\  |
      /    |
    _______|
    ""","""
    ________
       |   |
       O   |
      /|\  |
      / \  |
    _______|
    """]
    strikes = 0
    x = 0
    while strikes < 6:
        print(hangMan[x])
        guess = input("Enter a letter (guess in lowercase only): ")
        if guess in secretWord:
            print("Correct!")
        else:
            print("Wrong!")
            strikes += 1
            x += 1

    if strikes == 6:
        print(hangMan[6])
        print("GAME OVER! \n Going back to main menu...")

# show stat file
def showStats():
    file = open("stats.txt","r")
    print(file.read())

# put new player in stat file
def createPlayer():
    name = input("Enter player name: ")
    file = open("stats.txt", "a")
    file.write("Player name: " + name + "\n Total games played: \n Total wins: \n Total loses: \n Total ties: \n")
