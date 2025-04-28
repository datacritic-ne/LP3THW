# Making up a game
# Let's try a game based on Bill & Ted's Bogus Journey

# Begin with Bill and Ted being killed by their evil robot doppelgangers, and ending up in purgatory
# They then have to beat Death in 3 games
# Once they have Death on their side, they proceed to the Battle of the Bands, where they have to defeat the evil robots
# They defeat the robots by playing 80s metal

from sys import argv

script, user_name = argv

def start():
    print(f"Hi {user_name}. Do you want to play the game as Bill or Ted?")

    player = input("> ")

    if "Bill" in player:
        print("Excellent! *plays air guitar*\n")
    elif "Ted" in player:
        print("Greetings, Ted Theodore Logan Esquire!\n")
    else:
        print("Dude, who are you?")
        exit(0)

    print("Today, you two were busy flirting with your girlfriends and not practicing guitar.")
    print("Unfortunately, you were kidnapped by Evil Robot Us-es, who threw you from the top of a cliff.\n")

    print("Dude, I think we're dead.")
    print("This is the start of our most bogus journey.\n")
    
    death_game(player)

def death_game(player):
    games = ['Battleship', 'Chess', 'Clue', 'Baccarat', 'Twister', 'Bridge', 'Magnet football', 'Texas Hold Em']

    print("The world looks very bleached out, like through a blue camera lens filter.")
    print("The Angel of Death appears, and takes you both down to the netherworld.\n")
    
    if "Bill" in player:
        print("Dude, I don't think we can get out of here unless we play a game against Death.")
    else:
        print("Bogus. I think we need to play a game against Death.")

    #beat_death = False

    # The idea here is that you have to beat Death at 3 games, or you'll be in the netherworld forever

    print("Death says he will help you get back to save your babes, but first you have to beat him in some games.")
    print("Here are your choices: Battleship, Chess, Clue, Baccarat, Twister, Bridge, Magnet football, and Hold Em.\n")
    
    i = 0

    while i < 3:
        
        choice = input("Which game will you play? ")

        if "Chess" in choice or "Baccarat" in choice or "Bridge" in choice or "Hold Em" in choice:
            dead("Unfortunately Death is really good at this game, and you two are stuck in the netherworld.")
        elif "Battleship" in choice: # and not beat_death:
            print("Death glares at you. ' You sunk my battleship!' Excellent!\n")
        elif "Clue" in choice: # and not beat_death:
            print("It's Colonel Mustard in the study with the candlestick! Righteous!\n")
        elif "Twister" in choice: # and not beat_death:
            print("Death can't get his foot over to the red circle! *plays air guitar*\n ")
        else:
            print("Good choice: Death is awful at this game. Excellent!")
        
        i += 1
        
    print("Excellent! Death is on your side. Now it's on to the Battle of the Bands!\n")
        
    battle()

def battle():
    songs = ['Warrant', 'Poison', 'Pink Floyd', 'Selena Gomez', 'Aphex Twin', 'Brian Eno', 'David Bowie', 'Whitesnake', 'Iron Maiden']
    
    print("With Death's help you arrive quickly at the Battle of the Bands.")
    print("Evil Robot Bill and Ted are waiting with their evil robot band.\n")
    print("Your two bands will take turns playing songs, and the crowd will decide who wins each round. There are five rounds.\n")
    
    print("Here are the artists whose songs you can choose to play:")
    print("Warrant, Selena Gomez, Poison, David Bowie, Whitesnake, Aphex Twin, Iron Maiden, Brian Eno, Pink Floyd")
    
    # Can I do this as a for-loop that counts up each team's wins

    i = 0 # The number of rounds
    j = 0 # Bill and Ted's score
    k = 0 # The evil robots' score

 #   for i in range(0, 6):

 #       choice = input("What will you play? ")

 #       if "Selena Gomez" in choice or "David Bowie" in choice or "Aphex Twin" in choice or "Brian Eno" in choice or "Pink Floyd" in choice:
 #           print("Bogus! Evil robot us-es are way better at that tune than us!")
 #           k += 1
 #       else:
 #           print("Excellent! *plays air guitar* The Wyld Stallyns win this round!")
 #           j +=  1
        
 #       if k == 3:
 #           dead("Dude, we lost the Battle and the robots killed us.")
 #       else j == 3:
 #           win()
    
    while i < 5:

        choice = input("What will you play? ")

        if "Selena Gomez" in choice or "David Bowie" in choice or "Aphex Twin" in choice or "Brian Eno" in choice or "Pink Floyd" in choice:
            print(f"Bogus! Evil robot us-es are way better at that tune than us! Round {i} to the bad guys!")
            k += 1
        else:
            print(f"Excellent! *plays air guitar* The Wyld Stallyns win round {i}!")
            j += 1

        i += 1

    if k > j:
        dead("Dude, we lost the Battle of the Bands and the robots killed us. The future is lost!")
    else:
        win()


def dead(why):
    print(why, "This is totally bogus.")
    exit(0)

def win():
    print("The evil robot us-es and the bad guy from Lethal Weapon 2 are defeated! The babes and the universe are saved!")
    exit(0)

start()

