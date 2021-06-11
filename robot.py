class Robot:
    def __init__(self, name, weapon, attack_power, power_level):
        self.name = name
        self.health = 100
        self.weapon = weapon
        self.attack_power = attack_power
        self.power_level = power_level

    def attack(self, dinosaur):
        pass