# Some strange new stuff

# Define a string variable containing the days of the week
days = "Mon Tue Wed Thu Fri Sat Sun"
# Define a string variable containing the months Jan-Aug, formatted so they'll print on separate lines
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Printing a text string, and then the contents of the days variable
print("Here are the days:", days)
# Printing a text string, and then the contents of the months variable
print("Here are the months:", months)

# Printing a text string that prints 4 sentences onto 4 separate lines. The triple quotes appears to be what makes this possible.
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
