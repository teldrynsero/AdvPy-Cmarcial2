def order(numbers,letters):
    #sort lowest to highest: A, B, C
    #numbers = numbers.astype(int)
    numbers = list(map(int,numbers))
    numbers.sort()
    #print(numbers)
    numbers = list(map(str,numbers))
    #A = numbers[0]
    #B = numbers[1]
    #C = numbers[2]
    answer = 0

    #ABC - ACB - BAC - BCA - CBA - CAB
    if letters[0] == 'A':
        answer = numbers[0]
        if letters[1] == 'B':
            answer = answer + " " + numbers[1]
            answer = answer + " " + numbers[2]
        else: #letters[1] is C
            answer = answer + " " + numbers[2]
            answer = answer + " " + numbers[1]
        
    if letters[0] == 'B':
        answer = numbers[1]
        if letters[1] == 'A':
            answer = answer + " " + numbers[0]
            answer = answer + " " + numbers[2]
        else: #letters[1] is C
            answer = answer + " " + numbers[2]
            answer = answer + " " + numbers[0]

    if letters[0] == 'C':
        answer = numbers[2]
        if letters[1] == 'B':
            answer = answer + " " + numbers[1]
            answer = answer + " " + numbers[0]
        else: #letters[1] is A
            answer = answer + " " + numbers[0]
            answer = answer + " " + numbers[1]
    
    return answer

def start():
    numbers = input("")
    numbers = numbers.split(" ")

    letters = input("")
    letters = list(letters)

    #print(numbers)
    #print(letters)

    print(order(numbers,letters))

if __name__ == "__main__":
    start()