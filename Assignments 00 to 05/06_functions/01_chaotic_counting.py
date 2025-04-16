from random import random

# 0.0 to 1.0: jitna chhota number, utni zyada chance ke counting ruk jaye
DONE_LIKELIHOOD = 0.2  # 20% chance to stop at each number

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1

        if done():
            return
        print(curr_num)

def done():
    # Agar random number 0.2 se chhota hai, to stop
    if random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
