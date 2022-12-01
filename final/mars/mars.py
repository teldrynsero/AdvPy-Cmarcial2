import math
#Launch windows: April 2018, June 2020,
#August 2022, October 2024, December 2026,
#February 2029, April 2031...
#1,3,5,7,9,12,14
#Happens every 2 years 2 months (2.1666)

def launch(year):
    year = int(year)
    #2018: year 1, but starts in April (3 months of 2018 not included)
    year = (year-2017.333)
    answer = math.fmod(year,2.16666666666)
    if answer < 1:
        return "yes"
    else:
        return "no"

def start():
    year = input("")
    print(launch(year))

if __name__ == "__main__":
    start()