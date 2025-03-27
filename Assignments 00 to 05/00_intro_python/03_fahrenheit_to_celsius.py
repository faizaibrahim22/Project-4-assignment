def main():

   degrees_Fahrenhite = float(input("Enter temperature in Fahrenhite: "))

   degrees_celsius = (degrees_Fahrenhite - 32) * 5.0 / 9.0

   print(f"Temperature: {degrees_Fahrenhite}F= {degrees_celsius} C")
   
main()