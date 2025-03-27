import math


def main():
     ab:float = float(input("Enter the length of AB :"))
     ac:float = float(input("Enter the length of AC :"))

     bc:float= math.sqrt(ab**2 + ac**2)
     print(f"the length of BC ( the hypotense) is {bc}")
if __name__ == '__main__':
     main()