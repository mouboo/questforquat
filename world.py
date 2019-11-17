#world.py

import random
import enemies

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

class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is not a very interesting room.
        """

class VictoryTile(MapTile):
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

world_dsl = """
|  |VT|  |
|  |EN|  |
|EN|ST|EN|
|  |EN|  |
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
            row.append(tile_type(x,y) if tile_type else None)
        world_map.append(row)    

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
