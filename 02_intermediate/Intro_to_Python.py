# MERCURY_GRAVITY = 0.376 
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378 
# JUPITER_GRAVITY = 2.36 
# SATURN_GRAVITY = 1.081 
# URANUS_GRAVITY = 0.815 
# NEPTUNE_GRAVITY = 1.14 
# EARTH_GRAVITY = 1.0

# def main(): earth_weight_str = input('Enter a weight on Earth: ')

# # Get the numeric value since input() returns a value in string form
# earth_weight = float(earth_weight_str)

# # Having a variable for each piece of information is a good habit
# mars_weight = earth_weight * MARS_MULTIPLE
# rounded_mars_weight = round(mars_weight, 2)


# # Note the string concatenation!
# print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

# def main(): # Prompt the user for their weight on Earth 
#     earth_weight = float(input("Enter a weight on Earth: "))
# planet = input("Enter a planet: ")

# # Determine the gravitational constant for the selected planet
# if planet == "Mercury":
#     gravity_constant = MERCURY_GRAVITY
# elif planet == "Venus":
#     gravity_constant = VENUS_GRAVITY
# elif planet == "Mars":
#     gravity_constant = MARS_GRAVITY
# elif planet == "Jupiter":
#     gravity_constant = JUPITER_GRAVITY
# elif planet == "Saturn":
#     gravity_constant = SATURN_GRAVITY
# elif planet == "Uranus":
#     gravity_constant = URANUS_GRAVITY
# else:
#     # can assume user types in one of these planets, so this can be an else instead of elif
#     gravity_constant = NEPTUNE_GRAVITY

# # Calculate the equivalent weight on the selected planet
# planetary_weight = earth_weight * gravity_constant
# rounded_planetary_weight = round(planetary_weight, 2)

# # Print the result
# print("The equivalent weight on " + planet + ":  " + str(rounded_planetary_weight))
# if __name__ == "__main__": 
#     main()

# Gravitational constants relative to Earth's gravity
# Gravitational constants relative to Earth's gravity
# MERCURY_GRAVITY = 0.376
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378
# JUPITER_GRAVITY = 2.36
# SATURN_GRAVITY = 1.081
# URANUS_GRAVITY = 0.815
# NEPTUNE_GRAVITY = 1.14
# EARTH_GRAVITY = 1.0

# # Dictionary for planet gravity values
# gravity_constants = {
#     "Mercury": MERCURY_GRAVITY,
#     "Venus": VENUS_GRAVITY,
#     "Mars": MARS_GRAVITY,
#     "Jupiter": JUPITER_GRAVITY,
#     "Saturn": SATURN_GRAVITY,
#     "Uranus": URANUS_GRAVITY,
#     "Neptune": NEPTUNE_GRAVITY
# }

# def calculate_mars_weight(earth_weight):
#     """Calculates weight on Mars only"""
#     mars_weight = round(earth_weight * MARS_GRAVITY, 2)
#     print(f"The equivalent weight on Mars: {mars_weight}")

# def calculate_planetary_weight(earth_weight, planet):
#     """Calculates weight on any given planet"""
#     gravity_constant = gravity_constants.get(planet, None)

#     if gravity_constant is None:
#         print("Invalid planet name. Please enter a valid planet.")
#         return

#     planetary_weight = round(earth_weight * gravity_constant, 2)
#     print(f"The equivalent weight on {planet}: {planetary_weight}")

# def main():
#     """Main function to interact with the user"""
#     earth_weight = float(input("Enter a weight on Earth: "))

#     choice = input("Do you want to calculate weight on Mars only? (yes/no): ").strip().lower()
    
#     if choice == "yes":
#         calculate_mars_weight(earth_weight)
#     else:
#         planet = input("Enter a planet: ").strip().capitalize()
#         calculate_planetary_weight(earth_weight, planet)

# if __name__ == "__main__":
#     main()

# Gravitational constants relative to Earth's gravity
GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_weight(earth_weight, planet):
    """Calculates the equivalent weight on a given planet."""
    gravity_constant = GRAVITY_CONSTANTS.get(planet)

    if gravity_constant is None:
        print("Invalid planet name. Please enter a valid planet.")
        return

    planetary_weight = round(earth_weight * gravity_constant, 2)
    print(f"The equivalent weight on {planet}: {planetary_weight}")

def main():
    """Main function to interact with the user."""
    earth_weight = float(input("Enter your weight on Earth: "))

    # Ask for the planet
    planet = input("Enter a planet (e.g.,Mercury, Mars, Jupiter, Venus\n Saturn, Uranus, Neptune): ").strip().capitalize()

    # Calculate weight on the chosen planet
    calculate_weight(earth_weight, planet)

if __name__ == "__main__":
    main()
