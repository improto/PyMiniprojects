import random

def play(highest):
    randValue = random.randint(1,highest)
    userValue = 0

    while userValue != randValue:
        userValue = int(input("Enter your guess\t"))

        if userValue > randValue:
            print("Too high")
        if userValue < randValue:
            print("Too low")
    
    return 'Congratulations!!! You win!'


def autoGuess(randValue):

    compValue = random.randint(1,(randValue*randValue)) #higher limit set to square of the correct value
    count = 1

    while randValue != compValue:

        count = count + 1
        #if guess too high
        #reduce upper limit maintain lower limit
        if compValue > randValue:   #Reduce guessing range
            newRandom = compValue - 1
            compValue = random.randint(1, newRandom)
            print(compValue)
            
        #if guess too low   
        #increase lower limit and maintain higher limit
        if compValue < randValue:
            newRandom = compValue + 1
            compValue = random.randint(newRandom, randValue)   
            print(compValue)

    print(f"Guessed {count} times")
    return "Guessed"


#involves the user with the system guessing
def interactiveGuess():

    randValue = int(input("Enter number to be guessed\t"))

    compValue = random.randint(1,(randValue*randValue)) #higher limit set to square of the correct value
    count = 1

    while randValue != compValue:
        print(compValue)

        isCorrect = input(" 'h' for guess too high\n 'l' for guess too low\t").lower()
        
        #if guess too high
        if isCorrect == 'h':  
            newRandom = compValue - 1
            compValue = random.randint(1, newRandom)
            
        #if guess too low   
        if isCorrect == 'l':
            newRandom = compValue + 1
            compValue = random.randint(newRandom, randValue)   
        
        count = count + 1

    print(compValue)
    print(f"Guessed {count} times")
    return("Yay!!!Computer guessed the number")

print(interactiveGuess())