from animal import Animal

class Reptile(Animal): # Inheriting from animal class
    def __init__(self): # note the (self), if this is missing it can cause errors, check for this in exam
        super().__init__() # super is used to inherit everything from the parent class, this may come up in the exam
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "It's chilly looking have fun in the sun"

    def hunt(self):
        return "Keep working hard to find food"

    def use_venom(self):
        return "If I have it I will use it"

# Let's create an object of Reptile class
# smart_reptile = Reptile()
# print(smart_reptile.breathe()) # breathe method is inherited from Animal class
# print(smart_reptile.hunt()) # hunt() is available in Reptile class
# print(smart_reptile.eat())
# print(smart_reptile.move())
# print(smart_reptile.hunt())