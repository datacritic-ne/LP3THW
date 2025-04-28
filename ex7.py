# Prints first line of Mary had a little lamb
print("Mary had a little lamb.")
# Prints the second actual line - no Smashing Pumpkins reference - uses format string for 'snow'
print("Its fleece was white as {}.".format('snow'))
# Prints the 3rd line
print("And everywhere that Mary went.")
print("." * 10) # Assuming this prints an ellipsis ten periods long - correct

# the "end" variables are the 12 letters of Cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch end = ' ' at the end, try removing it to see what happens - Cheese and Burger are printed on separate lines
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # Prints the word 'Cheese' and a space after it, prevents a carriage return
print(end7 + end8 + end9 + end10 + end11 + end12) # Prints the word 'Burger'
