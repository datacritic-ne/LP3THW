the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# we can go through mixed lists the same way
for i in change:
    print(f"I got {i}")

# we can also build lists, by starting with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
    print(elements)

# now we can print them out
for i in elements:
    print(f"Element was: {i}")

# do this differently
elements2 = [0, 1, 2, 3, 4, 5]

for i in elements2:
    print(f"Element was: {i}")

          