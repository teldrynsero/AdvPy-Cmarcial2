#which dogs will attack which heroes?
def calculate(dog1,dog2,A,C,P,M,G):
    postAttacked = 0
    milkAttacked = 0
    garbageAttacked = 0

    #counter for how many dog attacks occur
    attack = 0

    #will the postman be attacked?
    #will the dog be attacking when the hero is present? 
    if P % dog1 <= A and P % dog1 > 0:
        attack += 1
    if P % dog2 <= C and P % dog2 > 0:
        attack += 1

    if attack == 0:
        postAttacked = "none"
        print("none")
    elif attack == 1:
        postAttacked = "one"
        print("one")
    elif attack == 2:
        postAttacked = "both"
        print("both")

    #reset
    attack = 0

    #will the milkman be attacked?
    if M % dog1 <= A and M % dog1 > 0:
        attack += 1
    if M % dog2 <= C and M % dog2 > 0:
        attack += 1

    if attack == 0:
        milkAttacked = "none"
        print("none")
    elif attack == 1:
        milkAttacked = "one"
        print("one")
    elif attack == 2:
        milkAttacked = "both"
        print("both")

    #reset
    attack = 0

    #will the garbage man be attacked?
    #4 % 2 = 0 <= 2 and > 0
    if G % dog1 <= A and G % dog1 > 0:
        attack += 1
    if G % dog2 <= C and G % dog2 > 0:
        attack += 1

    if attack == 0:
        garbageAttacked = "none"
        print("none")
    elif attack == 1:
        garbageAttacked = "one"
        print("one")
    elif attack == 2:
        garbageAttacked = "both"
        print("both")

    return postAttacked + "\n" + milkAttacked + "\n" + garbageAttacked

def start():
    #times dogs are active and calm
    dogIntervals = input("")
    dogIntervals = dogIntervals.split(" ")

    #dog 1 is aggressive
    A = int(dogIntervals[0])
    #dog 1 is calm
    B = int(dogIntervals[1])

    #dog 2 is aggressive
    C = int(dogIntervals[2])
    #dog 2 is calm
    D = int(dogIntervals[3])

    #time heroes arrive
    heroTimes = input("")
    heroTimes = heroTimes.split(" ")

    #postman arrives
    P = int(heroTimes[0])
    #milkman arrives
    M = int(heroTimes[1])
    #garbage man arrives
    G = int(heroTimes[2])

    #total dog times
    dog1 = A + B
    dog2 = C + D

    calculate(dog1,dog2,A,C,P,M,G)


if __name__ == "__main__":
    start()