class Song(object): # creating a class named Song with const and a fn

    def __init__(self, lyrics): # creating constructor , with lyrics parameter that will be passed
        self.lyrics = lyrics # putting lyrics to self.lyrics variable

    def sing_me_a_song(self): # creating a fn inside the class
        for line in self.lyrics: # accessing predefined const, line is variable
            print(line)

happy_bday = Song(["Happy birthday to you", # accessing the Song class, using const. lyrics is given ip
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
anthem = Song([" amar shonar Bangla \n ami tomay valobashi."])

happy_bday.sing_me_a_song()
lyr2 = "I walk this empty street on the boulevard of broken dreams."
broken_dreams = Song([lyr2])

lyrics1 = "esho he boishakh esho esho\n taposho nisshasho baye "
var1 = Song([lyrics1])

bulls_on_parade.sing_me_a_song()
anthem.sing_me_a_song()
broken_dreams.sing_me_a_song()
var1.sing_me_a_song()
