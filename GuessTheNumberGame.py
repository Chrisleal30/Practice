import random
number = random.randint(0,21)
guess = int(input("Pick a number between 0 & 20."))

while guess != number:
    if guess < number:
        print("Sorry, the number you have chosen is too low!")
        guess = int(input("Guess again!"))
    elif guess > number:
        print("Sorry, the number you have chosen is too high!")
        guess = int(input("Guess again!"))
    else:
        break

if guess == number:
    print("Nice, you've guessed the correct number!") 