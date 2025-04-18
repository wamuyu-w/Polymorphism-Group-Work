class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # default value, can be set to anything
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # setting a range of values from 0 to the max(when its full)
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        # finding the energy range for the pet when it sleeps
        self.energy = min(10, self.energy + 5)

    def play(self):
        # finding the energy level after playing
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def pet_information(self):
        # various pet information that will be outputted
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        # the pet is capable of having tricks e.g. rolling over, playing with balls
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")
