#enemies.py

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant spider"
        self.hp = 10
        self.damage = 2

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10

