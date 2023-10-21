class Zoo:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def output(self):
        return f"{self.name}, the {self.species}"

wolf = Zoo("Cookie", "wolf, grey, hawk")
chicken = Zoo("who names chickens?", "chicken, bird, can fly, herbivorous")
fox = Zoo("Berry", "fox, red, hawk")
giraffe = Zoo("Pinkie", "very tall, yellow with brown dots, herbivorous")
elephant = Zoo("Dumbo", "very big, grey, herbivorous")

a = input("please, enter one of these animals: wolf, chicken, fox, giraffe, elephant: ")

if a == "wolf":
    print(wolf.name)
    print(wolf.species)
elif a == "chicken":
    print(chicken.name)
    print(chicken.species)
elif a == "fox":
    print(fox.name)
    print(fox.species)
elif a == "giraffe":
    print(giraffe.name)
    print(giraffe.species)
elif a == "elephant":
    print(elephant.name)
    print(elephant.species)
elif a != "wolf" "chicken" "fox" "giraffe" "elephant":
    print("please, try again")