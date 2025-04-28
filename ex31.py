print("""You enter a dark room with two doors.
Do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Shout at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear bites your face off. Well done!")
    elif bear == "2":
        print("The bear bites your legs off. Well done!")
    else:
        print(f"Well, doing {bear} is probably a better idea.")
        print("The bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Well done!")
    else:
        print("The insanity rots your eyes into a puddle of muck.")
        print("Well done!")

elif door == "3":
    print("You enter the Double R diner in Twin Peaks. What to order?")
    print("1. A cherry pie that'll kill ya.")
    print("2. A damn fine cup of coffee.")
    print("3. A small box of chocolate bunnies.")

    order = input("> ")

    if order == "1":
        print("You are writing an epic poem about this pie!")
        print("Well done!")
    elif order == "2":
        print("DAMN good coffee! And HOT!")
        print("Well done!")
    else:
        print("It isn't about the bunnies at all.")
        print("Is it all about the bunnies?")

else:
    print("You stumble around and fall on a knife and die. Well done!")
