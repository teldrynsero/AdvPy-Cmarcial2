#get car positions at the 3 intervals
times = input("")
times = times.split(" ")

#difference between 2 and 1 intervals
difference1 = int(times[1]) - int(times[0])

#difference between 3 and 2 intervals
difference2 = int(times[2]) - int(times[1])

#print(difference1)
#print(difference2)

if difference1 > 0 and difference2 < 0 or difference1 < 0 and difference2 > 0:
    print("turned")
    exit()

difference1 = abs(difference1)
difference2 = abs(difference2)

if difference1 == difference2:
    print("cruised")

elif difference2 > difference1:
    print("accelerated")

elif difference1 > difference2:
    print("braked")

