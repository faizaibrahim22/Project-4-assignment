def main():
    curr_value = int(input("Enter a number: "))  # User se number input lena

    while curr_value < 100:  # Jab tak value 100 se choti hai, loop chalay ga
        curr_value = curr_value * 2  # Value ko double karna
        print(curr_value)  # Print karna

if __name__ == "__main__":
    main()
