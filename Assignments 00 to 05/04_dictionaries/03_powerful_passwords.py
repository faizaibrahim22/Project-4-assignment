from hashlib import sha256

def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password" ka hash
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # "Karel" ka hash
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"   # "123!456?789" ka hash
    }

    # Test cases to check the login function
    print(login("example@gmail.com", stored_logins, "word"))  # Expected: False
    print(login("example@gmail.com", stored_logins, "password"))  # Expected: True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Expected: True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Expected: False

    print(login("student@stanford.edu", stored_logins, "password"))  # Expected: False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Expected: True

if __name__ == '__main__':
    main()
