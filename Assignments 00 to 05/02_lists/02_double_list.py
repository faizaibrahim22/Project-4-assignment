def main():

    numbers : list[int] = [1,2,3,4,5] 
    numbers = [num * 2 for num in numbers]
    print(numbers)

if __name__ == "__main__":
    main()