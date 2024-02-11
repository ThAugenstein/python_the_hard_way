name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")

height_in_centimeters = round(height * 2.54)
weight_in_kilograms = round(weight / 2.205)
print("And now for all non US folks out there:")
print(f"He's {height_in_centimeters} centimeters tall.")
print(f"He's {weight_in_kilograms} kilograms heavy.")
