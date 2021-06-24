class Animal: # Follow the correct naming convention
    # We need to initialise with built in method called __init__(self)
    # self refers to current class
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive!"

    def eat(self):
        return "Time to eat"

    def move(self):
        return "Move left and right to stay awake"


# We need to create an object of this class in order to use any methods
# cat = Animal() # Creating an object of Animal class
# # For cat as a user the functionality inside Animal class and the method breathe is abstracted
# print(cat.breathe())