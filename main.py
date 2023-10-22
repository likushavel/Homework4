class Zoo:
    def __init__(self, animal, predator, height, fact):
        self.animal = animal
        self.predator = predator
        self.height = height
        self.fact = fact
        print("The object was created")

    def __str__(self):
        return f"I'm name {self.animal}. My age is {self.predator}. My height is {self.height}. My fact is that I`m {self.fact}"

    def __del__(self):
        print("Object is delete")

giraffe = Zoo("GIRAFFE", "Herbivorous", "Heidht: 4.2 cm","Tall animal" )
print(giraffe.animal)
print(giraffe.predator)
print(giraffe.height)
print(giraffe.fact)

tigger = Zoo("TIGGER", "Predactor", "Height: 80-110 cm", "Dangerous animal")
print(tigger.animal)
print(tigger.predator)
print(tigger.height)
print(tigger.fact)

jaguar = Zoo("JAGUAR", "Predactor", "Height: 80-110 cm", "Fast animal")
print(jaguar.animal)
print(jaguar.predator)
print(jaguar.height)
print(jaguar.fact)

koala = Zoo("KOALA", "Herbivorous", "Height: 60-85 cm", "Slow animal")
print(koala.animal)
print(koala.predator)
print(koala.height)
print(koala.fact)

