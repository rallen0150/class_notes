class Monster:
    def __init__(self):
        self.hp = 10


class Weapon:
    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):
        self.set_durability()
        return self.damage

    def set_durability(self):
        self.durability -= 1
        if self.durability < 0:
            self.durability = 0
            self.damage = 0

class Sword(Weapon):
    def __init__(self):
        self.damage = 3
        self.durability = 2

class UnbreakableSword(Sword):
    # No __init__ because I want to use the same as the sword class
    def set_durability(self):
        pass


orc = Monster()
bad_sword = Weapon()
ok_sword = Sword()
awesome_sword = UnbreakableSword()

print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
