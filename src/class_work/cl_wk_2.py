from os import name


class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl


    def action(self):
        return f"{self.name} base action"

class MagHero(Hero):
    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def spell_cast(self):
        return f"{self.name} spell cast"

kirito = Hero("kirito", 100, 100)
print(kirito.action())
asuno = MagHero("asuno", 100, 100, 1000)
print(asuno.action())


