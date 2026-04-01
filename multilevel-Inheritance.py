class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name, species = "Dog")
        self.breed= breed

    def showDetails(self):
        animal.showDetails(self)

class goldenRetriever(dog):
    def __init__(self,name, color):
        dog.__init__(self,name, breed="goldenRetiever")
        self.color = color

    def showDetails(self):
        dog.showDetails(self)
        print(f"Color:{self.color}")

g = goldenRetriever("Tommy","Black")
g.showDetails()
print(goldenRetriever.mro())