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

    if select == "A" or select == "a":
        #start new game

        #randomly chooses a word from the list
        randomChoose()

        #start game
        #startGame()

#################################################

    if select == "B" or select == "b":
        #end program
        print("Goodbye")
        exit()

#################################################

    if select=="C" or select == "c":
        #display player stats
        showStats()

#################################################

    if select=="D" or select == "d":
        #create new player
        createPlayer()