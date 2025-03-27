MINIMUM_HEIGHT : int = 50 # arbitrary units :)

def main():

    height = float(input("How tell are you:!"))
    if height >= MINIMUM_HEIGHT:
        print("You are tall to enougt to ride!")
    else:
        
        print("You're not tall enough to ride, but maybe next year!")
if __name__ == "__main__":
    main()
