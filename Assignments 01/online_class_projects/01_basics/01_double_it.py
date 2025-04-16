def main():
    curr_value = int(input("Enter a number: "))  # User se number lena
    
    while curr_value < 100:  # Jab tak number 100 se chhota hai
        curr_value *= 2  # Double karna
        print(curr_value)  # Print karna

if __name__ == "__main__":
    main()
