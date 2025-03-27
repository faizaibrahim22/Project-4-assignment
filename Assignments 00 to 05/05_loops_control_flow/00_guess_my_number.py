import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99:")

    try:
        guess = int(input("Enter a guess: "))

        while guess != secret_number:
            if guess < secret_number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")

            print()  # Print an empty line to tidy up the console for new guesses
            guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
        print("Congrats! The number was: " + str(secret_number))

    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
