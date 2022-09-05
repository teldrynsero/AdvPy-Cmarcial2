import random

gamesPlayed = 0
gamesWon = 0
gamesLost = 0

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

        #start game with random word
        startGame(secretWord)

#records player stats into stats.txt
def stats(gamesPlayed,gamesLost):
    totalGamesPlayed = str(gamesPlayed)
    totalGamesLost = str(gamesLost)
    f = open("stats.txt", "a")
    f.write("Total games played: " + totalGamesPlayed + "\n" "Total games lost: " + totalGamesLost + "\n")
    f.close()

# start the actual game after getting user input
def startGame(secretWord):
    print("Game starting...")
    #hangman images
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
    #counts amount of wrong guesses
    strikes = 0
    #hangman image counter
    x = 0

    #while there is no game over
    while strikes < 6:
        print(hangMan[x])
        guess = input("Enter a letter: ")

       #guess was a symbol or number; reject it and ask for input again
        if not guess.isalpha():
            print("Non-letter guesses are invalid: try again!")
        else:
            #guess is a letter
            if guess.lower() in secretWord:
                print("Correct!")
            else:
                print("Wrong!")
                strikes += 1
                x += 1

    #for letter in secretWord:
    #    print()

    #GAME OVER you lost
    if strikes == 6:
        #print the completely hanged man, game over
        print(hangMan[6])

        #increment player's games played and loses
        global gamesPlayed
        gamesPlayed += 1
        global gamesLost
        gamesLost += 1

        print("GAME OVER! \n")

    answer = input("Want to play again? y/n \n")
    if answer.lower() == 'y':
        print("Starting new game...")
        #start a new game with new word
        randomChoose()
    else:
        print("Thank you for playing hangman! \n Returning to main menu...")
        #record player stats from game
        stats(gamesPlayed,gamesLost)

# show stat file
def showStats():
    file = open("stats.txt","r")
    print(file.read())

# put new player in stat file
def createPlayer():
    name = input("Enter player name: ")
    file = open("stats.txt", "a")
    file.write("Player name: " + name + "\n")
