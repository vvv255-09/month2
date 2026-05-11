from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hp, lvl, st):
        self.name = name
        self.__hp = hp
        self.lvl = lvl
        self.st = st

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def rest(self):
        self.__hp += 1
        print(f"{self.name} отдыхает... {self.__hp}")

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"Воин {self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"Маг {self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")

samurai = Warrior("King-Artur", 1000, 175, 10000)
koldun = Mage("Merlin", 800, 115, 220)
ninja = Assassin("Anbu", 900, 155, 7700)

for hero in [samurai, koldun, ninja]:
    hero.greet()
    hero.attack()
    hero.rest()