class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name , species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark !")
        print(f"The breed is {self.breed}")

d = dog ("Dog","Labrador")
d.make_sound()

a = animal("Dog","Dog")
a.make_sound()
