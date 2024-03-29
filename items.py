#items.py

import art

# Weapons
class Weapon:
    def __init__(self):
        raise NotImplementedError("Don't create raw Weapon objects.")
        self.description = "There's nothing interesting about it."

    def __str__(self):
        return"{} (+{} damage)".format(self.name, self.damage)        

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

# Consumables
class Consumable:
    def __init__(self):
        raise NotImplementedError("Don't create raw Consumable objects")
        self.description = "There's nothing interesting about it."

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
        self.name = "Bowl of oats"
        self.healing_value = 20
        self.value = 5

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60

# Wearable - upper
class WearableUpper:
    def __init__(self):
        raise NotImplementedError("Don't create raw WearableUpper objects.")
        self.description = "There's nothing interesting about it."

    def __str__(self):
        return"{} (+{} armor)".format(self.name, self.armor_value)

class ChristmasSweater(WearableUpper):
    def __init__(self):
        self.name = "Christmas Sweater"
        self.description = "A colourful green and red wool christmas sweater."
        self.armor_value = 10
        self.value = 30

class Blouse(WearableUpper):
    def __init__(self):
        self.name = "Blouse"
        self.description = "A white blouse from Odd Molly."
        self.armor_value = 5
        self.value = 80

class Robe(WearableUpper):
    def __init__(self):
        self.name = "Robe"
        self.description = "A nice robe."
        self.armor_value = 10
        self.value = 80

# Wearable - lower
class WearableLower:
    def __init__(self):
        raise NotImplementedError("Don't create raw WearableLower objects.")
        self.description = "There's nothing interesting about it."

    def __str__(self):
        return"{} (+{} armor)".format(self.name, self.armor_value)

class YogaPants(WearableLower):
    def __init__(self):
        self.name = "Pair of Yoga Pants"
        self.description = "Black yoga pants."
        self.armor_value = 1
        self.value = 20

class Jeans(WearableLower):
    def __init__(self):
        self.name = "Pair of Jeans"
        self.description = "A pair of comfy jeans."
        self.armor_value = 4
        self.value = 15

# Wearable - head
class WearableHead:
    def __init__(self):
        raise NotImplementedError("Don't create raw WearableLower objects.")
        self.description = "There's nothing interesting about it."
        
    def __str__(self):
        return"{} (+{} armor)".format(self.name, self.armor_value)

class Headband(WearableHead):
    def __init__(self):
        self.name = "Headband"
        self.description = "A grey soft headband with a bow in the front."
        self.armor_value = 5
        self.value = 15

class WizardsHat(WearableHead):
    def __init__(self):
        self.name = "Wizards Hat"
        self.description = "A big wizards hat with a pointy tip."
        self.armor_value = 5
        self.value = 50

# Special items

class MallMap:
    def __init__(self):
        self.name = "Mall Map"
        self.description = art.mall_map
        self.value = 2
        
    def __str__(self):
        return self.name

class ScrubDaddy:
    def __init__(self):
        self.name = "Scrub Daddy"
        self.description = ("A circular hard sponge in the shape of a "
                           "yellow smiley")
        self.value = 20
        
    def __str__(self):
        return self.name

# Books
class Book:
    def __init__(self):
        raise NotImplementedError("Don't create raw Book objects.")
        self.description = "There's nothing interesting about it"

    def __str__(self):
        return self.name

class BookofQuat(Book):
    def __init__(self):
        self.name = "Book of Quat"
        self.description = "A leather bound book with a big star on the front."
        self.value = 100

class PoetryBook(Book):
    def __init__(self):
        self.name = "Poetry from around the world"
        self.description = "some poems"
        self.value = 10

class HouseOfLeavesBook(Book):
    def __init__(self):
        self.name = "House of Leaves"
        self.description = "The book seems larger on the inside somehow."
        self.value = 8