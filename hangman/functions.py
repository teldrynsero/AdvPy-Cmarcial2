import random

from playsound import playsound

#for tracking player stats
gamesPlayed = 0
gamesWon = 0
gamesLost = 0

#reset counters
def reset():
    global gamesPlayed
    gamesPlayed = 0
    global gamesWon
    gamesWon = 0
    global gamesLost
    gamesLost = 0

#randomly chooses word
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

    #reset game counters
    reset()
    

#hangman game
def startGame(secretWord):
    print("Game starting...")
    playsound('start.wav')
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
    #letters the player correctly guesses
    lst2 = []
 
    #split secret word into letters
    for letter in secretWord:
        lst.append(letter)

    #create array to show player how many letters to guess
    for letter in secretWord:
        lst2.append("_")

    #while player still has guesses left...
    while strikes < 6:
        #print(lst)
        #print(lst2)

        #show hangman pictures
        print(hangMan[x])
        #show secret word length
        print(' '.join(lst2))
        guess = input("Enter a letter: ")
        guess = guess.lower()

       #guess is symbol or number (reject)
        if not guess.isalpha():
            print("Non-letter guesses are invalid: try again!")
            playsound('wrong.wav')
        else:
            #guess is a letter (accept)
            if guess in secretWord:
                print("Correct!")
                playsound('correct.wav')

                while guess in lst:
                    #get index of guess
                    guessIndex = lst.index(guess)

                    #reveal index to player
                    lst2.pop(guessIndex)
                    lst2.insert(guessIndex,guess)

                    #remove corresponding index from secret word
                    lst.remove(guess)
                    lst.insert(guessIndex,"0")

                #see if all letters guessed
                s = set(lst)
                if (len(s) == 1):
                    print("\n All letters guessed correctly!")
                    strikes = 7 #get out of loop
                else:
                    print("Still letters to guess left...")
            else:
                print("Wrong!")
                playsound('wrong.wav')
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
        playsound('win.wav')

    #GAME OVER you lost
    if strikes == 6:
        #print the completely hanged man, game over
        print(hangMan[6])

        #increment player's loses
        global gamesLost
        gamesLost += 1

        print("GAME OVER! \n The secret word was " + secretWord)
        playsound('lost.wav')

    answer = input("Want to play again? y/n \n")
    if answer.lower() == 'y':
        #start a new game with new word
        randomChoose()
    else:
        print("Thank you for playing hangman! \n Returning to main menu...")
        playsound('exit.wav')
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
    file.write("\n" + "Player name: " + name + "\n")
