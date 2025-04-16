import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE
        print(random.randint(MIN_VALUE, MAX_VALUE))

if __name__ == '__main__':
    main()
