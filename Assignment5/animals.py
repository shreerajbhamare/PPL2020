class Animals:
    def habitat(self):
        pass

    def sounds(self):
        pass

    def food(self):
        pass

    def color(self):
        pass

class Herbivores(Animals):
    def food(self):
        print("I eat herbs and plants")

class Carnivores(Animals):
    def food(self):
        print("I eat other animals")

class Omnivores(Animals):
    def food(self):
        print("I eat both plants and other animals")

class Wild(Animals):
    def habitat(self):
        print("I love in the wild jungles")

class Domestic(Animals):
    def habitat(self):
        print("I live inside houses with humans")

class Dog(Omnivores, Domestic):
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I bark")

    def color(self):
        print("I am mostly brown, black, white or golden")

class Cat(Omnivores, Domestic):
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I meow")

    def color(self):
        print("I am mostly brown, black, white or golden")

class Lion(Carnivores, Wild):
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I roar")

    def color(self):
        print("I am golden")

class Tiger(Carnivores, Wild):
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I roar")

    def color(self):
        print("I am orange with black stripes")

class Fish(Herbivores, Wild):
    def __init__(self, legs = 0, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I make no sounds")

    def color(self):
        print("I come in all colors")

class Hamster(Herbivores, Domestic):
    def __init__(self,  legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I squeak")

    def color(self):
        print("I am mostly black, brown, white or golden")

class Horse(Herbivores, Domestic):
    def __init__(self,  legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I neigh")

    def color(self):
        print("I am mostly black, brown or white")

    def habitat(self):
        print("I live in stables")

class Jackal(Carnivores, Wild):
    def __init__(self,  legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I laugh")

    def color(self):
        print("I am red")

class Bear(Omnivores, Wild):
    def __init__(self,  legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)

    def sounds(self):
        print("I growl")

    def color(self):
        print("I am brown, white or black")

class Cow(Herbivores, Domestic):
    def __init__(self,  legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
        print("I am a ", self.__class__.__name__)
    
    def sounds(self):
        print("I moo")

    def color(self):
        print("I am white or brown")

cow = Cow()
cow.habitat()
horse = Horse()
horse.sounds()
fish = Fish()
fish.food()
tiger = Tiger()
tiger.color()