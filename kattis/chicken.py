input = input("")

input = input.split(" ")

#input[0]: people at buffet
#input[1]: chickens

people = int(input[0])
chicken = int(input[1])

#print(people)
#print(chicken)

answer = chicken - people

if answer >= 0:
    if answer == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        answer = str(answer)
        print("Dr. Chaz will have " + answer + " pieces of chicken left over!")
elif answer < 0:
    moreChicken = people - chicken
    if moreChicken == 1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        moreChicken = str(moreChicken)
        print("Dr. Chaz needs " + moreChicken + " more pieces of chicken!")