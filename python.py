from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "I can digest anything without chewing"

    def climb(self):
        return "Up we go!"

    def __shed_skin(self):
        return "Bye skin"

fast_python = Python()
print(fast_python.__)
print(fast_python.digest_large_prey())
print(fast_python.hunt())
print(fast_python.shed_skin())