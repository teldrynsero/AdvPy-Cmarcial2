#input[0]: people at buffet
#input[1]: chickens

def output(answer, moreChicken):
    if answer >= 0:
        if answer == 1:
            return "Dr. Chaz will have 1 piece of chicken left over!"
        else:
            answer = str(answer)
            return "Dr. Chaz will have " + answer + " pieces of chicken left over!"
    elif answer < 0:
        #moreChicken = people - chicken
        if moreChicken == 1:
            return "Dr. Chaz needs 1 more piece of chicken!"
        else:
            moreChicken = str(moreChicken)
            return "Dr. Chaz needs " + moreChicken + " more pieces of chicken!"

def calculate(people, chicken):
    #more chicken than people:
    answer = chicken - people
    #more people than chicken:
    moreChicken = people - chicken

    print(output(answer, moreChicken))
    return output(answer,moreChicken)

def start():
    #get people and chicken input
    userInput = input("")
    userInput = userInput.split(" ")

    people = int(userInput[0])
    chicken = int(userInput[1])

    calculate(people, chicken)

#userInput = input("")
#start(userInput)

if __name__ == "__main__":
    start()