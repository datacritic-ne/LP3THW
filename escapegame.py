from sys import exit
from textwrap import dedent

# The idea here is to mimic an escape room
# Scenario: you're invited to a dinner party in a mansion with 2 other guests, and the host is killed. You have to solve the murder and not get killed.
# In each room you have to solve 3 puzzles, maybe 3 rooms? So 9 total puzzles to solve
# First: the killer locks you in the dining room, and you have to get the doors open
# Second: you're out of the dining room, but 1 of the other guests is the killer. You need to find a cellphone to call the police.
# Third: the police are on their way, but you need to figure out which of the guests is the killer.
# I don't like the random numbers from the textbook game. I'd prefer math or logic puzzles, or codes.

# Scene class initialization - will this work without this class?
class Scene(object):
    def enter(self):
        print("Scene not yet configured.")
        print("Subclass with enter().")
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

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print("Unfortunately you did not solve the murder, and now you can only hope that someone else will solve yours.")
        exit(1)

class DiningRoom(Scene):

    def enter(self):
        print(dedent("""
            One afternoon you get a knock at the door, and are presented with an invitation to a dinner party thrown by Dr. Fitzwater Brigadoon.
            He lives in a large mansion on the outskirts of town, and is well-known as a deeply eccentric millionaire inventor.
            You have no idea why you've received this invitation, but you're intrigued and you agree to go.\n
            You arrive early in the evening, and are shown into a long dining hall by the butler.
            There are two other guests: 
            """))
        pass

class MainHall(Scene):

    def enter(self):
        pass

class Study(Scene):

    def enter(self):
        pass

class Finished(Scene):

    def enter(self):
        print("You solved the murder! Well done!")
        return 'finished'

class Map(object):

    scenes = {
        'dining_room': DiningRoom(),
        'main_hall': MainHall(),
        'study': Study(),
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
    

a_map = Map('dining_room')
a_game = Engine(a_map)
a_game.play()
