def main():
    # Dictionary with fruit names as keys and their prices as values
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Variable to keep track of the total cost
    
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the fruit
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
        # Calculate the cost for this fruit and add it to the total
        total_cost += (price * amount_bought)
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")

# This line calls the main() function to start the program
if __name__ == '__main__':
    main()
