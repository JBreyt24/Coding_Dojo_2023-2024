



class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)
        return self



class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()



my_treats = ["Tuna Bites", "Cat Nip", "Shrimp Snacks"]
my_pet_food = ["Fancy Feast", "Kibbles & Bits"]

ms_fuzz = Pet("Ms. Fuzz", "Cat", "Pounces", "Meow")

josh = Ninja("Josh", "Breytspraak", my_treats, my_pet_food, ms_fuzz)

josh.feed()

josh.walk()

josh.bathe()