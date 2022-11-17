def sign(birthday):
    birthday = birthday.split(" ")
    #print(birthday)
    
    #for x in birthdays:
    #    #print(x)
    #    splitBirthday = birthdays[x].split(" ")
    #    print(splitBirthday)

    if birthday[1] == "Jan":
        if 1 <= int(birthday[0]) <= 20:
            return "Capricorn"
        else:
            return "Aquarius"

    elif birthday[1] == "Feb":
        if 1 <= int(birthday[0]) <= 19:
            return "Aquarius"
        else:
            return "Pisces"

    elif birthday[1] == "Mar":
        if 1 <= int(birthday[0]) <= 20:
            return "Pisces"
        else:
            return "Aries"

    elif birthday[1] == "Apr":
        if 1 <= int(birthday[0]) <= 20:
            return "Aries"
        else:
            return "Taurus"

    elif birthday[1] == "May":
        if 1 <= int(birthday[0]) <= 20:
            return "Taurus"
        else:
            return "Gemini"

    elif birthday[1] == "Jun":
        if 1 <= int(birthday[0]) <= 21:
            return "Gemini"
        else:
            return "Cancer"

    elif birthday[1] == "Jul":
        if 1 <= int(birthday[0]) <= 22:
            return "Cancer"
        else:
            return "Leo"

    elif birthday[1] == "Aug":
        if 1 <= int(birthday[0]) <= 22:
            return "Leo"
        else:
            return "Virgo"

    elif birthday[1] == "Sep":
        if int(birthday[0]) <= 21:
            return "Virgo"
        else:
            return "Libra"

    elif birthday[1] == "Oct":
        if int(birthday[0]) <= 22:
            return "Libra"
        else:
            return "Scorpio"

    elif birthday[1] == "Nov":
        if int(birthday[0]) <= 22:
            return "Scorpio"
        else:
            return "Sagittarius"

    elif birthday[1] == "Dec":
        if int(birthday[0]) <= 21:
            return "Sagittarius"
        else:
            return "Capricorn"

def start():
    classmates = input("")
    classmates = int(classmates)

    x = 0
    birthdays = []

    for i in range(0,classmates):
        #ele = str(input())
        ele = 0
        birthdays.append(ele)

    #sign(birthdays)

    #print(birthdays[0])

    while classmates != 0:
        birthday = input("")
        birthdays[x] = sign(birthday)
        x = x + 1
        classmates = classmates - 1

    for x in birthdays:
        print(x)
        

if __name__ == "__main__":
    start()