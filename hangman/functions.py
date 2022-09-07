import random

#for tracking player stats
gamesPlayed = 0
gamesWon = 0
gamesLost = 0

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
def stats(gamesPlayed,gamesLost,gamesWon):
    totalGamesPlayed = str(gamesPlayed)
    totalGamesLost = str(gamesLost)
    totalGamesWon = str(gamesWon)
    f = open("stats.txt", "a")
    f.write("Total games played: " + totalGamesPlayed + "\n Total games lost: " + totalGamesLost + "\n Total games won: " + totalGamesWon)
    f.close()

#hangman game
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

    #list of letters in secret word
    lst = []
 
    for letter in secretWord:
        lst.append(letter)
 
    #see secret word for debugging
    #print(lst)

    #while player still has guesses left
    while strikes < 6:
        print(hangMan[x])
        guess = input("Enter a letter: ")
        guess = guess.lower()

       #guess was a symbol or number; reject it and ask for input again
        if not guess.isalpha():
            print("Non-letter guesses are invalid: try again!")
        else:
            #guess is a letter
            if guess in secretWord:
                print("Correct!")
                while guess in lst:
                    lst.remove(guess)
                    print(lst)

                if len(lst) == 0:
                    print("All letters guessed!")
                    strikes = 7 #get out of loop
                else:
                    print("Still guesses left")
            else:
                print("Wrong!")
                strikes += 1
                x += 1

    global gamesPlayed
    gamesPlayed += 1

    #YOU WIN
    if strikes == 7:
        #increment player's wins
        global gamesWon
        gamesWon += 1

        print("YOU WON! \n The secret word was " + secretWord)

    #GAME OVER you lost
    if strikes == 6:
        #print the completely hanged man, game over
        print(hangMan[6])

        #increment player's loses
        global gamesLost
        gamesLost += 1

        print("GAME OVER! \n The secret word was " + secretWord)

    answer = input("Want to play again? y/n \n")
    if answer.lower() == 'y':
        print("Starting new game...")
        #start a new game with new word
        randomChoose()
    else:
        print("Thank you for playing hangman! \n Returning to main menu...")
        #record player stats from game
        stats(gamesPlayed,gamesLost,gamesWon)

# show stat file
def showStats():
    file = open("stats.txt","r")
    print(file.read())

# put new player in stat file
def createPlayer():
    name = input("Enter player name: ")
    file = open("stats.txt", "a")
    file.write("Player name: " + name + "\n")
