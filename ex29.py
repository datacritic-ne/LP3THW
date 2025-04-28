people = 20
cats = 10
dogs = 3

if people < cats: # If executes the command below if the condition is met, and ignores that command otherwise
    print("Too many cats! The world is doomed!") # The print statement must be indented; returns IndentationError otherwise.

if people > cats:
    print("Not many cats! The world is saved!") # The indentation signals a block of code associated with the if statement; otherwise Python can't tell where the code continues on after the if.

if people < dogs:
    print("The world is drooled upon!")

if people > dogs:
    print("The world is dry!")

if people > dogs and people > cats:
    print("Y\'all really need more pets in your life.")

  #  print("Does this show why indentation is needed?") YES

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if people != dogs:
    print("No, we're not dogs.")

