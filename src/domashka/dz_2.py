import random

# Родительский|Супер класс
class Hero:
    def __init__(self, name, hp, lvl, st):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.st = st

    def greet(self):
        print("hello!")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.st -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.hp += 1

class Warrior(Hero):

    def __init__(self, name, hp, lvl, st, stamina):
        super().__init__(name, hp, lvl, st)
        self.stamina = stamina

    def greet(self):
        print(f"{self.name} hello!")

    def attack(self):
        print(f"Воин {self.name} наносит удар мечом!")


# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, hp, lvl, st, mp):
        super().__init__(name, hp, lvl, st)
        self.mp = mp

    def greet(self):
        print(f"{self.name} hello!")

    def attack(self):
        print(f"Маг {self.name} активировал заклинание!!")

class Assasin(Hero):
    def __init__(self, name, hp, lvl, st, stealth):
        super().__init__(name, hp, lvl, st)
        self.stealth = stealth

    def greet(self):
        print(f"{self.name} hello!")

    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка")



chubakabra = Assasin("Chubakabra", 153, 889, 9754, 8283)
zhelmoguz = MageHero("Zhelmoguz", 196, 794, 10879, 7891)
chypalak = Warrior("Chypalak-Batyr", 851, 1000, 100089, 1234567)

chubakabra.attack()
zhelmoguz.attack()
chypalak.attack()





heroes = ["Warrior", "Mage", "Assassin"]

winner = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior"
}
try:
    ch = input("Выберите героя: Warrior / Mage / Assassin: ").strip().capitalize()

    if ch not in heroes:
        print("Неверный герой, попробуй снова!")


    opponent = random.choice(heroes)

    print(f"Вы выбрали: {ch}")
    print(f"Противник: {opponent}")

    if winner[ch] == opponent:
        print(f"{ch} победил!")
    elif winner[opponent] == ch:
        print(f"{opponent} победил!")
    else:
        print("Ничья!")
except:
    print("Выберите из имеюшихся")
