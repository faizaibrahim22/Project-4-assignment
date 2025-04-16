# Planet ke gravity constants
planet_gravity = {
    'Mercury': 0.376,
    'Venus': 0.889,
    'Mars': 0.378,
    'Jupiter': 2.36,
    'Saturn': 1.081,
    'Uranus': 0.815,
    'Neptune': 1.14
    
}

# User se Earth weight aur planet ka naam lo
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Chosen planet ka gravity constant nikalo
gravity_constant = planet_gravity.get(planet)

# Check if the planet is in the dictionary
if gravity_constant:
    # Planet pe weight calculate karo
    planet_weight = earth_weight * gravity_constant
    # Result ko 2 decimal places tak round karo
    planet_weight_rounded = round(planet_weight, 2)
    print(f"The equivalent weight on {planet}: {planet_weight_rounded}")
else:
    print("Planet not recognized.")
