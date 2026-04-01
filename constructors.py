class person:
    def __init__(self,name,occ):
        self.name = name
        self.occ =  occ
        print("Hey I am a person")

    def info (self):
        print(f"{self.name} is a {self.occ}")

a = person("Harry","HR")
a.info()