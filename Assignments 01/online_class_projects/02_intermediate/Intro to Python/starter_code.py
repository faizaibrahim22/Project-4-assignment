"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Gravity constants for different planets (as percentages of Earth's gravity)
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Step 1: Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: Prompt the user for the planet's name
    planet = input("Enter a planet: ")

    # Step 3: Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        # If the planet name is not recognized, inform the user
        print("Planet not recognized.")
        return

    # Step 4: Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant

    # Step 5: Round the result to 2 decimal places
    rounded_planetary_weight = round(planetary_weight, 2)

    # Step 6: Display the result
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")

if __name__ == "__main__":
    main()
