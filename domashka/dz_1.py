class Hero:

    def __init__(self, name, lvl, hp, st):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.st = st

    def greet(self):
        print(f"Мое имя {self.name}, мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.st -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.hp += 1


chubakabra = Hero("Chubakabra", 153, 889, 9754)
zhelmoguz = Hero("Zhelmoguz", 196, 794, 10879)
chypalak = Hero("Chypalak-Batyr", 851, 1000, 100089)

for hero in [chubakabra, zhelmoguz, chypalak]:
    hero.greet()
    hero.attack()
    print(f"Сила после атаки: {hero.st}")
    hero.rest()
    print(f"Здоровье после отдыха: {hero.hp}")
    print()