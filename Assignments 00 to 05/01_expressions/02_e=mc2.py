C = 299792458  # Speed of light in meters per second

def main():
    mass_in_Kg = float(input("Enter kilos of mass: "))  # Input mass from user
    energy_in_joules = mass_in_Kg * (C**2)  

    # Output the result
    print("e = m * C^2...")
    print("m = " + str(mass_in_Kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    main()
