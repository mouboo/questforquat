#player.py

import items
import world
import os

class Player:
    def __init__(self):
        self.inventory = [items.CoffeeCup(),
                          items.CoffeeCup(),
                          items.Oats(),
                          items.Blouse(),
                          items.Jeans(),
                          items.Dagger()
                         ]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 500
        self.victory = False
        self.wear_upper = items.ChristmasSweater()
        self.wear_lower = items.YogaPants()
        self.wear_head = items.Headband()
        self.current_weapon = items.RolledMagazine()

    def is_alive(self):
        return self.hp > 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0,dy=-1)

    def move_south(self):
        self.move(dx=0,dy=1)

    def move_east(self):
        self.move(dx=1,dy=0)

    def move_west(self):
        self.move(dx=-1,dy=0)

    def print_inventory(self):
        while True:
            os.system('cls||clear')
            print('#' * 34 + ' INVENTORY ' + '#' * 35)
            print('In your Herschel backpack you have:')
            if self.gold > 0:
                print("  * Money: {} crowns".format(self.gold))
            if self.inventory:
                for item in self.inventory:
                    print('  * ' + str(item))
            print('')
            wearing_now = []
            for w in [self.wear_head,self.wear_upper,self.wear_lower]:
                if w:
                    wearing_now.append(w)
            if not wearing_now:
                print("You are not wearing any clothes >.>")
            else:
                print("You're wearing:")
                for item in wearing_now:
                    print('  * ' + str(item))
            print('')
            print("You're carrying a {} as a weapon".format(self.current_weapon))
            print('')
 
            while True:
                print(('Would you like to (E)xamine an item, ' 
                       '(W)ield a weapon, (C)hange clothes,\n'
                       'or (Q)uit inventory?'))
                user_input = input('> ')
                if user_input in ['Q','q']:
                    return
                elif user_input in ['E','e']:
                    examinables = self.inventory[:]
                    examinables.extend([self.wear_upper, self.wear_lower,
                                        self.wear_head, self.current_weapon])
                    if not examinables:
                        input("You have nothing to examine. " +
                                "Press enter to continue")
                        break
                    print("Choose item to examine, or (Q)uit examining")
                    for i, item in enumerate(examinables, 1):
                        print("{}. {}.".format(i,item))
                    choice = input('> ')
                    if choice in ['q','Q']:
                        break
                    try:
                        to_examine = examinables[int(choice) - 1]
                        print(to_examine.description)
                        print("Press enter to continue")
                        input()
                        break
                    except (ValueError,IndexError):
                        input("Invalid choice, press enter to continue.")
                        break
                elif user_input in ['W','w']: # Wield weapon
                    weapons = [item for item in self.inventory
                               if isinstance(item, items.Weapon)]
                    if not weapons:
                        input("You don't have any other weapons. " + 
                              "Press enter to continue.")
                        break
                    print("Choose weapon to wield, or (Q) to quit: ")
                    for i, item in enumerate(weapons, 1):
                        print("{}. {}.".format(i, item))
                    choice = input('> ')
                    if choice in ['q','Q']:
                        break
                    try:
                        to_wield = weapons[int(choice) - 1]
                        self.inventory.append(self.current_weapon)
                        self.current_weapon = to_wield
                        self.inventory.remove(to_wield)
                        print('You wield a ' + to_wield.name + '.')
                        input('Press enter to continue')
                        break
                    except (ValueError,IndexError):
                        input("Invalid choice, press enter to continue.")
                        break
                elif user_input in ['C','c']: # Change clothes
                    wearables = [item for item in self.inventory
                                if isinstance(item, items.WearableUpper) or
                                isinstance(item, items.WearableLower) or
                                isinstance(item, items.WearableHead)]
                    if not wearables:
                        input("You don't have any other clothes. " + 
                              "Press enter to continue.")
                        break
                    print("Choose what to wear, or (Q) to quit: ")
                    for i, item in enumerate(wearables, 1):
                        print("{}. {}".format(i, item))
                    choice = input('> ')
                    if choice in ['Q','q']:
                        break
                    try:
                        to_wear = wearables[int(choice) - 1]
                        if isinstance(to_wear, items.WearableUpper):
                            self.inventory.append(self.wear_upper)
                            self.wear_upper = to_wear
                            self.inventory.remove(to_wear)
                            print('You put on a ' + to_wear.name + '.')
                            input('Press enter to continue')
                            break
                        elif isinstance(to_wear, items.WearableLower):
                            self.inventory.append(self.wear_lower)
                            self.wear_lower = to_wear
                            self.inventory.remove(to_wear)
                            print('You put on a ' + to_wear.name + '.')
                            input('Press enter to continue')
                            break
                        elif isinstance(to_wear, items.WearableHead):
                            self.inventory.append(self.wear_head)
                            self.wear_head = to_wear
                            self.inventory.remove(to_wear)
                            print('You put on a ' + to_wear.name + '.')
                            input('Press enter to continue')
                            break
                        else:
                            print("Error: Unknown type of wearable")
                    except (ValueError,IndexError):
                        print("Invalid choice, press enter to continue.")
                        input('')
                        break
                              
    def pick_up_item(self):
        room = world.tile_at(self.x, self.y)
        flooritems = [item for item in room.floor_items]
        print("Choose item to pick up, or (Q) to quit: ")
        for i, item in enumerate(flooritems, 1):
            print("{}. {}.".format(i, item))
        choice = input('> ')
        if choice in ['q','Q']:
            return
        try:
            to_pick_up = flooritems[int(choice) - 1]
            self.inventory.append(to_pick_up)
            room.floor_items.remove(to_pick_up)
            print('You pick up a ' + to_pick_up.name + '.')
            input('Press enter to continue')
            return
        except (ValueError,IndexError):
            input("Invalid choice, press enter to continue.")
            return

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x,self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name,enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name,enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you.")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i,item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError,IndexError):
                print("Invalid choice, try again.")
    
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)