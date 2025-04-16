def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)  # Yeh print ab function ke andar hai


def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid number.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst  # Yeh ab while loop ke baad sahi jagah pe hai


def main():
    lst = get_list_of_ints()
    count_even(lst)  # Function ka sahi naam


if __name__ == '__main__':
    main()
