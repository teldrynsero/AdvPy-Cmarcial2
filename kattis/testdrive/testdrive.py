#what did the car do?
def calculate(difference1,difference2):
    if difference1 > 0 and difference2 < 0 or difference1 < 0 and difference2 > 0:
        print("turned")
        return "turned"

    difference1 = abs(difference1)
    difference2 = abs(difference2)

    if difference1 == difference2:
        print("cruised")
        return "cruised"

    elif difference2 > difference1:
        print("accelerated")
        return "accelerated"

    elif difference1 > difference2:
        print("braked")
        return "braked"

def start():
    #get car positions at the 3 intervals
    times = input("")
    times = times.split(" ")

    #difference between 2 and 1 intervals
    difference1 = int(times[1]) - int(times[0])

    #difference between 3 and 2 intervals
    difference2 = int(times[2]) - int(times[1])

    calculate(difference1,difference2)

if __name__ == "__main__":
    start()