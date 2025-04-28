# import the argv function
from sys import argv

# specifying a .py script and a file name as arguments for argv
script, filename = argv

# printing a formatted string with the filename.
print(f"We're going to erase {filename}.")
# printing a couple of meaningless strings (I think - does ctrl-C actually work here?)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

# taking user input regarding the erasing question
input("?")

# printing a short string indicating that the file is being opened
print("Opening the file ... ")
# creating a variable for the opened text file, and specifying that the open file is write-capable
target = open(filename, 'w')

# printing a short string indicating that the old file is being overwritten
print("Truncating the file. Goodbye!")
# calling the truncate or erase command on the open file object
target.truncate() # Interestingly this may be redundant with the 'w' option specified in the open command

# printing a short string indicating that new text will be requested for the file.
print("Now I'm going to ask you for three lines.")

# specifying 3 variables for user input to each of the 3 lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# printing a short string indicating that the new lines will be written to the file.
print("I'm going to write these to the file.")

# Six lines calling the write function on the open file object. Writing each line and inserting a carriage return after each one
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Rewriting the file writing sequence as a single command
target.write(line1 + '\n' + line2+ '\n' + line3 + '\n')

#printing a short string indicating that the file will now be closed.
print("And finally, let's close it.")
# calling the close command on the open file object
target.close()
