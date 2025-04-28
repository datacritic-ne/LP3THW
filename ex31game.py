# A preview of things to come

print("Welcome to the Monty Hall Problem, er Game.")
print("Monty shows you three doors.")
print("Behind one of the doors is a brand new Range Rover. Behind the other two are goats.")

print("Monty asks you to pick a door. Which would you like: 1, 2 or 3?")

door1 = input("> ")

if door1 == "1":
    print("Monty walks over to door #3, and opens it. There is a confused-looking goat staring out.")
    print("Monty asks you whether you want to change your pick to door #2, or stick with door #1.")

    door2 = input("> ")

    if door2 == "1":
        print("I hope you have room at home for the goat that is behind door #1.")
        print("Better luck next time!")
    else:
        print("VROOOOOOMMMM!!!!!!!!!!")

elif door1 == "2":
    print("Monty walks over to door #3, and opens it. There is a confused-looking goat staring out.")
    print("Monty asks you whether you want to change your pick to door #1, or stick with door #2.")

    door3 = input("> ")

    if door3 == "1":
        print("VROOOOOOMMMMMMM!!!!!!!!!!!")
    else:
        print("I hope you have room at home for the goat that is behind door #2.")
        print("Better luck next time!")

elif door1 == "3":
    print("Monty walks over to door #2, and opens it. There is a confused-looking goat staring out.")
    print("Monty asks you whether you want to change your pick to door #1, or stick with door #3.")

    door4 = input("> ")

    if door4 == "1":
        print("VROOOOOOMMMMMMM!!!!!!!!!!!")
    else:
        print("I hope you have room at home for the goat that is behind door #3.")
        print("Better luck next time!")

else:
    print("I don't know what game you're playing, but Monty requires a different answer. Try again!")
    