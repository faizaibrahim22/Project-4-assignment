MAX_LENGTH: int = 3  # Set MAX_LENGTH to 3 as per the requirement

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Loop till the list has more than MAX_LENGTH elements
        last_elem = lst.pop()  # Remove and get the last element of the list
        print(last_elem)  # Print the removed element

# User input function to get the list from the user
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Keep asking for input until the user presses Enter without typing anything
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Shorten the list to MAX_LENGTH by removing items from the end

if __name__ == '__main__':
    main()
