#####  PROJECT 2  GUESSES NUMBER GAME  #######

import random

def guess_number():
    number = random.randint(1, 100)
    guesses_left = 7

    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("I AM THINKING OF A NUMBER BETWEEN 1 TO 100.")

    while guesses_left > 0:
        print(f"\nYOU HAVE {guesses_left} guesses left.")
        
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input: please enter a valid number.")
            continue

        if guess == number:
            print(f"Congratulations! You guessed the number {number} correctly!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        guesses_left -= 1

    if guesses_left == 0:
        print(f"Sorry, you've run out of guesses. The number was {number}.")

# Run the game
guess_number()
