def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions.")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Extra credit puzzle below
print("Here is a puzzle:")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#what = divide(age, multiply(height, subtract(weight, add(age, 40))))

print("That becomes", what, ". Can you do it by hand?")
# Sure. Divide 50/2 = 25. Multiply 180*25 = 4500. Subtract 74-4500 = -4426. Add 35+-4426=-4391

print(35+(74-(180*(50/2))))
