# importing argv function so we can start with 2 inputs to the program
from sys import argv

# specifying that argv takes the script name and the text file name as inputs
script, filename = argv

# specifying a variable for the opened text file
txt = open(filename)

# printing a short formatted string that names the file we opened
print(f"Here's your file {filename}.")
# directing Python to read the contents of the text file, and then print those contents
print(txt.read())

txt.close()

# printing a short string instructing the user to input the text file name again
print("Type the filename again:")
# creating a variable that captures user input of the text file name
file_again = input("> ")

# specifying a variable for the opened (again) text file
txt_again = open(file_again)

# directing Python to read the contents of the text file again, and then print those contents
print(txt_again.read())

txt_again.close()


