from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
# this class doesn't actually do much, but illustrates how to make a base class
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. Well done.",
        "It's game over, man, game over!",
        "How's it hanging, Death?",
        "Well, you died. I hope you're happy.",
        "You died on that ship. Is there really anything more to say?"
    ]
    
    def enter(self):
        #print("It's game over, man, game over!") #should probably add a why # i like mine better, but 
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    # This is where the game begins
    def enter(self):
        # blah blah, print stuff introducing the game
        # there's a Gothon here, has to be defeated "with a joke". otherwise you die i guess
        print("Welcome to the starship Callister, Player X. Unfortunately, the Callister has been taken over by evil aliens called Gothons.\n")
        print("You are standing in the Central Corridor of the ship.\n")
        print("The good news is that you have a plan: enter the weapon armory, grab one of the neutron bombs you keep in there, plant it, and get away in an escape pod.")
        print("The bad news is that a green, ugly, 8-foot-tall Gothon is standing between you and the armory. He is drooling and looks very hungry.\n")
        #print("Still, this might be your lucky day. The Gothon will die if you make him laugh, but somehow he still has a sense of humor.")
        #print("He asks you: 'What is black, white, and red all over?'\n")
        #print("What do you say? 1. 'A newspaper' Or 2. 'A fight between Newcastle and Juventus fans'")
        print("Do you shoot, dodge, or tell a joke?")

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                You pull your blaster and get off the first shot. Unfortunately, your shot grazes his uniform but doesn't hurt him.
                The Gothon flies into a rage and bites your head off.
                """))
            return 'death'
        
        elif action == "dodge":
            print(dedent("""
                You bob and weave like a prizefighter as the Gothon steps towards you.
                Unfortunately you are pretty clumsy, and you slip in the hallway.
                Before you can stand again, the Gothon stomps on your head.
                """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
                Luckily for you the Gothon has a wicked sense of humor. Your joke stops him cold.
                He starts to laugh, and while he's laughing you shoot him squarely in the head.
                You then run past through the weapon armory door.
                """))
            return 'laser_weapon_armory'
        
        else:
            print("No comprendo")
            return 'central_corridor'

        #if joke1 == 2: #this works and sends you to the armory
        #    pass
        #else: #this goes to death
        #    pass

class LaserWeaponArmory(Scene):

    def enter(self):
        # this is where you come after the Central Corridor, you have to guess a number to get the neutron bomb
        # i guess you just keep giving it guesses until you get the bomb. not really a way to die here based on the description
        #print("Brilliant! The Gothon tries to hold it together, but a couple of giggles later he's disintegrated into a pile of green goo.\n")
        print("You race down the corridor and reach the armory door.")
        print("It has a simple keypad, and you only have to guess a three-digit number.")
        print("But if you guess wrong 10 times, the keypad will lock you out.")
        print("At that point it's just a matter of waiting for a Gothon to eat you. No pressure.")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZZZZZT! Try again.")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == 999:
            return 'the_bridge'

        elif guess == code:
            print(dedent("""
                The container clicks open and gas escapes.
                You grab the neutron bomb and run quickly out to the bridge to place it.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and you hear a melting sound as its mechanism fuses together.
                As you sit there, the Gothons blow up the ship from their ship, and you along with it.
                """))
            return 'death'

        #key == 6

        #guess1 = int(input("OK, what is your first guess? "))

        #if guess1 == key:
        #    pass # this works and sends you to the bridge
        #else:
        #    guess2 = int(input("That wasn't it. Take another guess: "))

        #    if guess2 == key: #this works and sends you to the bridge
        #        pass
        #    else:
        #        guess3 = int(input("That wasn't it either. Only one more try: "))

        #        if guess3 == key #this works and sends you to the bridge
        #            pass
        #        else:
        #            pass #you die here

class TheBridge(Scene):

    def enter(self):
        # battle another Gothon, I guess another joke? otherwise you die. but if you win you place the bomb and get away
        #print("That was it! The armory doors slide open, and you pull one of the neutron bombs off the shelf.")
        #print("Kind of surprising how easy it is to carry a neutron bomb.\n")
        #print("You run back down the corridor towards the bridge. Hopefully no one is there and you can place the bomb and get out of here.\n")
        print("The bridge doors open and ... another giant, ugly Gothon is sitting in the captain's chair, and he sees you immediately when you enter.\n")
        print("If you're going to place the bomb and get out of here, you need to deal with this Gothon the same way you dealt with the first one.\n")
        #print("The Gothon asks you: 'Do you have Prince Harry in a can?'")
        #print("What do you say? 1. 'A newspaper'. 2. 'Well, you'd better let him out!' 3. 'Well, he's seen the bottom of plenty of those in his life.'")

        #joke2 = int(input("> "))

        #if joke2 == 3:
        #    pass #this is the one that works
        #else:
        #    pass # this goes to death

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                You hastily throw the bomb at the Gothon and try to run for the door.
                The Gothon shoots you in the back as you run.
                You die, but die knowing that the Gothon will probably trigger the bomb trying to defuse it.
                """))
            return 'death'
        
        elif action == "slowly place the bomb":
            print(dedent("""
                The Gothon stops when he sees the bomb under your arm, and you point your blaster at it as you
                carefully place it on the floor by the door. You keep your blaster aimed at the bomb and inch
                back towards the door. Quickly you jump out, punch the close button, and shoot the lock so the
                Gothon can't get you. You then run to the escape pod.
                """))
            return 'escape_pod'
        else:
            print("No comprendo")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        # this is the "winning" condition
        #print("Success! The Gothon starts laughing and disintegrates into green goo.\n")
        #print("You place the neutron bomb under the captain's chair and set the timer to 60 seconds.")
        #print("You then duck into the escape pod room, lock yourself into a pod, and blast off.")
        #print("A minute later the Callister bursts into a giant ball of fire.")
        #print("You then settle in for the long trip home. Hopefully there are some good movies on DVD in this escape pod.")
        #exit(0)
        print(dedent("""
                Fortunately you see no Gothons as you reach the escape pod chamber. Some of the pods may be damaged, but 
                you don't have time to inspect. There are 5 pods: which one do you choose?
                """))
        
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} and hit eject.
                The pod blasts away from the ship, then implodes as the hull ruptures, killing you.
                """))
            return 'death'
        else:
            print(dedent(f"""
                You jump into pod {guess} and hit eject. The pod fires away from the ship towards a planet nearby.
                As it flies there, you look back and see the Callister explode, taking out the Gothon ship in the process.
                You win!
                """))
            return 'finished'
        
class Finished(Scene):

    def enter(self):
        print("Well done!")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
