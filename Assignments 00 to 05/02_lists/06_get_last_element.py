
def get_last_element(lst: list) -> None:
    print(lst[-1])  # Directly accessing the last element

def get_lst() -> list:
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)  # Corrected indentation here
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    get_last_element(lst)  # Print the last element

if __name__ == "__main__":
    main()
