#items.py

class Weapon:
    def __init__(self):
        raise NotImplementedError("Don't create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A small-ish rock."
        self.damage = 5
        self.value = 3

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust."
        self.damage = 10
        self.value = 20

class RolledMagazine(Weapon):
    def __init__(self):
        self.name = "Rolled up magazine"
        self.description = "A rolled up magazine"
        self.damage = 2
        self.value = 3

class Consumable:
    def __init__(self):
        raise NotImplementedError("Don't create raw Consumable objects")

    def __str__(self):
        return"{} (+{} HP)".format(self.name, self.healing_value)

class CoffeeCup(Consumable):
    def __init__(self):
        self.name = "Coffee Cup"
        self.description = "A tall cinnamon flavored cafe latte on oat milk."
        self.healing_value = 20
        self.value = 5

class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 10

class Oats(Consumable):
    def __init__(self):
        self.name = "A bowl of oats"
        self.healing_value = 20
        self.value = 5

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60