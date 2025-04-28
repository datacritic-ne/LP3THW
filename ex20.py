from sys import argv

script, input_file = argv

def print_all(f): # Defines a function print_all, with an input file as its argument
    print(f.read()) # Calls the read function on the file, and prints the contents

def rewind(f): # Defines a function rewind, with an input file as its argument
    f.seek(0) # Calls the seek function and returns Python's reference point to the beginning of the file

def print_a_line(line_count, f): # Defines a function print_a_line with a line count variable and an input file as arguments
    print(line_count, f.readline(), end=" ") # Prints the line_count number and reads the corresponding line

# Creates a variable that opens the input file test.txt
current_file = open(input_file)

# Printing a short string describing what the print_all function will do
print("First let's print the whole file:\n")

# Calls the print_all function with test.txt as its input, printing the read file
print_all(current_file)

# Printing a short string describing what the rewind function will do
print("Now let's rewind, like a tape.")

# Calls the rewind function with test.txt as its argument, to return Python's reference point to the beginning of the file
rewind(current_file)

# Printing a short string describing what the print_a_line function will do
print("Let's print 3 lines.")

# Creating a variable called current_line and specifying a value of 1
current_line = 1
# calling the "print a line" function, to print line 1 from test.txt
print_a_line(current_line, current_file)

# Advancing the current_line variable from 1 to 2
current_line += 1
# calling the "print a line" function, to print line 2 from test.txt
print_a_line(current_line, current_file)

# Advancing the current_line variable from 2 to 3
current_line += 1
# calling the "print a line" function, to print line 3 from test.txt
print_a_line(current_line, current_file)
