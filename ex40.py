class Song(object):

    def __init__(self, lyrics):
    
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        print self.lyrics
            
my_lyrics = ["Happy birthday to you","I don't want to get sued","So I'll stop right there"]

my_lyrics2 = ["They rally around the family","With pockets of shells"]
happy_bday = Song(raw_input("what's the lyrics for your happy birthday song? > "))

bulls_on_parade = Song(raw_input("Have something else to add? > "))

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()