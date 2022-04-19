class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("bark")
        return self

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food,
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

        

pet1 = Pet("Clifford", "dog", "flip", 0, 0)
ninja1 = Ninja("Tommy", "Bautista", "bone", "kibble", pet1.name)

