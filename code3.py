# Movie
class interstellar:
    iQ = 90
    strength = 75
    character_type = 'versetile'

    def __init__(self, name):
        self.name = name
        print("I belong to interstellar")
    def introduce(self):
        print("Hey my name in this movie is {}".format(self.name))
    def survive(self):
        print("Hey i have survived")
    def update_strength(self, value):
        self.strength = value
        print("The new updated strength is {}".format(self.strength))
    def update_iQ(self, value):
        self.iQ = value
        print("The new iQ value is {}".format(self.iQ ))

# Inheritance
class inception(interstellar):
    # interstellar -> parent_class  &  inception -> child_class
    # The methods and the attributes of the class interstellar are inherited to the class inception
    
    # Method overriding -> overriding the method from the parent class
    def __init__(self, name):
        self.name = name
        print("I belong to the inception")
    
    def dream(self):
        print("Hey i am dreaming.")

murf = interstellar('murf')
murf.introduce()
murf.survive()
murf.update_strength(98)
murf.update_iQ(97)
print('-'*30)

cooper = inception('cooper')
cooper.introduce()
cooper.survive()
cooper.update_strength(90)
cooper.update_iQ(70)
cooper.dream()