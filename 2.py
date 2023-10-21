class Cars:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def output(self):
        return f"{self.name}, the {self.species}"

juke = Cars("Nissan Juke", "release year - 2016, colour - yellow, horsepower - 188")
q5 = Cars("Audi Q5", "release year - 2022, colour - black, horsepower - 220")
x = Cars("Tesla Model X", "elon is jackass, don't buy tesla")
fiat = Cars("Fiat Multipla", "release year - 2000, gorgeous design, colour - blue, horsepower - 102")
kuga = Cars("Ford Kuga", "release year - 2019, colour - white, horsepower - 150")

a = input("please, enter one of these numbers: 1 for nissan juke, 2 for audi q5, 3 for tesla model x, 4 for fiat multipla, 5 for ford kuga: ")

if a == "1":
    print(juke.name)
    print(juke.species)
elif a == "2":
    print(q5.name)
    print(q5.species)
elif a == "3":
    print(x.name)
    print(x.species)
elif a == "4":
    print(fiat.name)
    print(fiat.species)
elif a == "5":
    print(kuga.name)
    print(kuga.species)
elif a != "1" "2" "3" "4" "5":
    print("please, try again")