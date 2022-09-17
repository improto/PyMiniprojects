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

print(play(20))