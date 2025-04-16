import random  # Random number generate karne ke liye

# Kitne rounds khelne hain
NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Score ko 0 se shuru karte hain

    # Har round ke liye loop chalana
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # User aur computer ke liye random numbers generate karte hain
        user_number = random.randint(1, 100)  # 1 se 100 tak random number
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")  # User ka number dikhana

        # User se guess lena (higher ya lower)
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Agar input galat ho, to user ko dobara input dena
        while guess not in ['higher', 'lower']:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Guess ko check karna
        if (guess == 'higher' and user_number > computer_number) or (guess == 'lower' and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Agar guess sahi hai to score mein 1 add karenge
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  # Round ke baad ek khaali line dena

    # Game ke end par score aur result dikhana
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Main function ko run karna
if __name__ == '__main__':
    main()
