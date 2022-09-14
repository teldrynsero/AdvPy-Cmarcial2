from functions import randomChoose, startGame, createPlayer, showStats

from playsound import playsound

select = True

#display options menu
while select:
    print("""
    === Hangman Game ===
    A: New Game
    B: Quit Game
    C: Player Status
    D: Create New Player
    """)

    playsound('menu.wav')

    #ask for user's choice
    select = input("Choose an option: ")

#################################################

    if select.lower() == "a":
        #start new game
        #randomly chooses a word from the list
        randomChoose()

#################################################

    if select.lower() == "b":
        #end program
        print("Exiting program...")
        playsound('exit.wav')
        exit()

#################################################

    if select.lower() == "c":
        playsound('select.wav')
        #display player stats
        showStats()

#################################################

    if select.lower() == "d":
        playsound('select.wav')
        #create new player
        createPlayer()