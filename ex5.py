name = 'Nick Emptage'
age = 49
height = 74 # in
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.454
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches (or {height_cm} centimeters) tall.")
print(f"He's {weight} pounds (or {weight_kg} kilograms).")
print("Actually that's not very heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# tricky here
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
