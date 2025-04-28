formatter = "{} {} {} {}" # Creates a string variable called formatter, which takes 4 arguments. Passing >4 arguments to formatter doesn't break the code, but <4 arguments does

print(formatter.format(1, 2, 3, 4)) # Passes 4 numbers to the format function of formatter, and prints them
print(formatter.format("one", "two", "three", "four")) # Passes 4 string numbers to the format function of formatter, and prints them
print(formatter.format(True, False, False, True)) # Passes 4 Boolean arguments to the format function of formatter, and prints them
print(formatter.format(formatter, formatter, formatter, formatter)) # Passes the formatter string (4 brackets) to the format function of formatter, and prints them. So, 4 sets of 4 brackets are printed
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) # Passes 4 text strings to the format function of formatter, and prints them. The 4 strings are broken onto 4 lines for readability.
