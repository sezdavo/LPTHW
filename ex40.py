# creating a class called song
class Song(object):
    # using init to initialize newly created empty object
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # creating function that prints song lines
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# instantiate 
happy_bday = Song(["Happy birthday to you",
                    "I dont want to get sued",
                    "so Ill stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
