import random

works = ["enum", "python", "collab", "vscode", "game"]

# Pick a random word from the works list
word = random.choice(works)
guessed_letters = []
attempts = 6

print("Welcome to the Hangman game project!")
print("__" + " " * len(word))  # Display underscores for the word

while attempts > 0:
    # Display the current guessed word (with underscores)
    current_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Current word: " + current_word)

    guess = input("\nGuess the letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please write one alphabet only!")
        continue

    if guess in guessed_letters:
        print("This letter is already guessed. Choose another letter.")
        continue
    
    guessed_letters.append(guess)

    if guess in word:
        print(f"Good guess! The letter '{guess}' is in the word.")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
    
    # Check if the word is fully guessed
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You've guessed the word:", word)
        break

else:
    print("Sorry, you've run out of attempts. The word was:", word)
