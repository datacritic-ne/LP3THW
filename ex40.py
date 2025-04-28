class Song(object):

    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(f"The artist behind this song is: {self.artist}\n")
        print(f"The name of this song is: {self.title}\n")
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "With a pocket full of shells."])

good_vibes = Song(["I'm pickin up good vibrations",
                   "She's givin me sweet sensations."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

good_vibes.sing_me_a_song()

riders_storm = ["Riders on the storm\n", "Like a dog without a bone\n", "An actor out on loan\n", "Riders on the storm\n"]

sing_riders = Song(riders_storm)
sing_riders.sing_me_a_song()

