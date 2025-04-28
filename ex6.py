# Defining a variable indicating that there are 10 types of people
types_of_people = 10
# Defining a format string stating the number of types of people
x = f"There are {types_of_people} types of people."

# Defining a string variable "binary"
binary = "binary"
# Defining a string variable for "don't"
do_not = "don't"
# Defining a format string bringing the 2 string variables into a sentence.
y = f"Those who know {binary} and those who {do_not}."

# Printing the "there are x types of people" string
print(x)
# Printing the second format string with the joke
print(y)

# Restating the first string
print(f"I said: '{x}'")
# Restating the second string, so the joke is clear
print(f"I also said: '{y}'")

# Defining a Boolean variable set to False
hilarious = False
# Defining a string variable with a format that evaluates the joke
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the joke evaluation string and format displaying the evaluation
print(joke_evaluation.format(hilarious))

# Defining a string variable w
w = "This is the left side of ..."
# Defining a string variable e
e = "a string with a right side."

# Printing w and e to demonstrate what happens when 2 string variables are added together
print(w + e)
