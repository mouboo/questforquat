#world.py

import random
import enemies
import npc
import items

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead.")

    def modify_player(self,player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a room with lots of plants.
        There are candles burning.
        There are doors in the north, south, east, and west directions.
        """

class HallwayTile(MapTile):
    def intro_text(self):
        return """
        You're in a busy mall hallway. 
        """

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see the quat!
        Victory is yours!
        """

class EnemyTile(MapTile):
    def __init__(self,x,y):
        r = random.random()
        if r < 0.5:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down at you!"
            self.dead_text = "The corpse of a dead spider lies on the ground."
        elif r < 0.8:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "There's a dead ogre."
        else:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "There's a giant spider here!"
            self.dead_text = "There's a dead spider here."

        super().__init__(x,y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage,player.hp))

class TraderTile(MapTile):
    def __init__(self,x,y):
        self.trader = npc.Trader()
        super().__init__(x,y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['B','b']:
                print("Here's what's available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S','s']:
                print("Here's what's available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice.")

    def trade(self,buyer,seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q','q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller,buyer,to_swap)
                except ValueError:
                    print("Invalid choice.")

    def swap(self,seller,buyer,item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")
    
    def intro_text(self):
        return """
        A store owner stands behind a counter. He looks willing to trade.
        """

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Nothing interesting to see here.
            """
        else:
            return """
            Someone dropped some gold. You pick it up.
            """

class HnMTile(TraderTile):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.trader.inventory = [items.Oats()]

    def intro_text(self):
        return """
        This is an H&M store
        """

    

world_dsl = """
|TT|VT|TT|TT|TT|TT|
|TT|HW|HW|HW|HW|TT|
|TT|HW|TT|TT|HW|TT|
|TT|HW|TT|TT|FG|TT|
|TT|HW|HW|HW|HW|TT|
|TT|TT|TT|TT|ST|HM|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "TT": TraderTile,
                  "FG": FindGoldTile,
                  "HW": HallwayTile,
                  "HM": HnMTile,
                  "  ": None}  

world_map = []

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x,y) if tile_type else None)
        world_map.append(row)    

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
