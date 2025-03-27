def read_phone_numbers():
    # Initialize an empty dictionary to store phonebook entries
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break  # Exit loop when the user inputs an empty string
        number = input("Number: ")
        phonebook[name] = number  # Store the name and number in the dictionary

    return phonebook  # Return the phonebook dictionary after the loop ends

def print_phonebook(phonebook):
    # Print all entries in the phonebook
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    # Lookup phone numbers by name
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit loop when the user inputs an empty string
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(f"Phone number for {name}: {phonebook[name]}")

def main():
    # Main function to run the phonebook operations
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
