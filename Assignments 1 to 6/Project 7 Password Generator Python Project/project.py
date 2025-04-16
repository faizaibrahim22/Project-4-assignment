import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long."

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
