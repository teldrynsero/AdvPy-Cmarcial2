from functions import randomChoose, startGame, createPlayer, showStats

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
        print("Goodbye")
        exit()

#################################################

    if select.lower() == "c":
        #display player stats
        showStats()

#################################################

    if select.lower() == "d":
        #create new player
        createPlayer()