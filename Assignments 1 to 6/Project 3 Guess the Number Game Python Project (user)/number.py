import random

number = random.randint(1,100)
print("Guess  the number between 1 to 100")

while True:
    guess =int(input(" Enter your a guess number"))

    if guess < number:
        print(" To Low  Number")
    elif guess > number:
        print("To high Number")
    else:
        print("Congratulation You got  it right!")
        break