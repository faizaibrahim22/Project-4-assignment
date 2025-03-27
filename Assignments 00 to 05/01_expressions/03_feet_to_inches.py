INCHES_IN_FOOT=12

def main():
    feet = float(input("Enter number of feet:"))
    inches = feet * INCHES_IN_FOOT
    print("That is feet",inches,"inches!")

if __name__ == '__main__':
    main()