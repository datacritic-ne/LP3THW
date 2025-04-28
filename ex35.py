from sys import exit

def gold_room():
    print("This room is full of gold. How much will you take?")

    choice = int(input("> "))
    #if "0" in choice or "1" in choice:
    #   how_much = int(choice)
    #else:
    #    dead("Dude, learn to type a number.")

    if choice < 50:
        print("Nice, you're not greedy, you win.")
        exit(0)
    else:
        dead("You are a bit greedy.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if "take honey" in choice:
            dead("The bear looks at you and then slaps your face off.")
        elif "taunt bear" in choice and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif "taunt bear" in choice and bear_moved: # The code will pretty much always skip this, because bear_moved is still False
            print("The bear gets pissed and chews your leg off.")
        elif "open door" in choice and bear_moved: # The code will skip this until you've taunted the bear, because bear_moved = False until that
            gold_room()
        else:
            print("No idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your own head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, I hope that tasted good.")
    else:
        cthulhu_room()

def chess_room():
    print("You enter to see the Angel of Death sitting at a table in front of a chess board.")
    print("Will you agree to play Death in chess?")

    choice = input("> ")

    if "y" in choice:
        print("What strategy will you play?")

        strategy = input("> ")

        if "sicilian" in strategy:
            print("Checkmate! You get to live!")
        else:
            dead("Sadly, Death is pretty good at chess.")

    else:
        dead("Unfortunately, the only other game Death will play is Battleship, which you lose.")


def dead(why):
    print(why, "Good job.")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right, one in the middle, and another to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if "left" in choice:
        bear_room()
    elif "right" in choice:
        cthulhu_room()
    elif "middle" in choice:
        chess_room()
    else:
        dead("You somehow starve.")

start()

