print("Let's count some chickens:")

# For Hens, 30/6 = 5 + 25 = 30
print("Hens", float(25 + 30 / 6))

# For Roosters, 25*3 = 75. 75 % 4 = 3. 100 - 3 =97
print("Roosters", float(100 - 25 * 3 % 4))

print("Now let's count some eggs:")

# 4 % 2 = 0. 1/4 = 0.25. So 1 + 0 - 0.25 + 6 = 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

# 3 + 2 = 5 is not < 5 - 7 = -2
print(3 + 2 < 5 - 7)

# Printing 3 + 2 = 5
print("What is 3 + 2?", 3 + 2)
# Printing 5 - 7 = -2
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's false.")

print("How about some more?")

# Print logical of 5 > -2 = TRUE
print("Is it greater?", 5 > -2)
# Print logical of 5 >= -2 = TRUE
print("Is it greater or equal?", 5 >= -2)
# Print logical of 5 <= -2 = FALSE
print("Is it less or equal?", 5 <= -2)
