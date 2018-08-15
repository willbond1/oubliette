class Creature:
    def __init__(self, name, hp, atk, shield, desc=''):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.atk = atk
        self.shield = shield
    
    def __str__(self):
        return """
        {}
        {}
        HP: {}
        """.format(self.name, self.desc, self.hp)

    def __repr__(self):
        return """
        Name: {}
        Desc: {}
        HP: {}
        ATK: {}
        DEF: {}""".format(self.name, self.desc, self.hp, self.atk, self.shield)

    def attack(self, enemy):
        pass

class Player(Creature):
    pass

class Monster(Creature):
    pass

class Game:
    pass