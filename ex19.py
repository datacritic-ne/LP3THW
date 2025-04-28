def cheese_and_crackers(cheese_count, boxes_of_crackers): # defining a function c&c that takes 2 arguments
    print(f"You have {cheese_count} cheeses!") # Printing a formatted string listing the number of cheeses inputted to the function
    print(f"You have {boxes_of_crackers} boxes of crackers!") # Printing a formatted string listing how many boxes of crackers have been inputted to the function
    print("Man, that's enough for a party!") # Printing a silly statement.
    print("Get a blanket.\n") # Printing another silly statement

# Printing a statement about running the function with numbers we feed it directly.
print("We can just give the function numbers directly:")
# Calling the c&c function with 2 numeric inputs
cheese_and_crackers(20, 30)

# Printing a statement about running the function with variable inputs we define before calling the function
print("OR, we can use variables from our script:")
# Defining a variable specifying how much cheese will be used by the function
amount_of_cheese = 10
# Defining a variable specifying how many boxes of crackers will be used by the function
amount_of_crackers = 50

# Calling the c&c function, using the prior 2 defined variables as its argument inputs
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Printing a statement about running the function with math inputs
print("We can even do math inside:")
# Calling the c&c function, with 2 mathematical arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Printing a statement about running the function with both variable and numeric inputs
print("And we can combine both approaches, variables and math:")
# Calling the c&c function, with 2 arguments that combine a defined variable + a number
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
