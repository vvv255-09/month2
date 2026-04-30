# OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы. git и github,

class Hero:
    #Контруктор класса
    def __init__(self, name, lvl, hp):

        #Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    
    def action(self):
        return f"{self.name} base action"

#обьект/экземпляр на основе класса
kirirto = Hero("Kirito", 100, 1000)
asuno = Hero("Asuno", 101, 1001)
chypalak = Hero("Chypalak", 102, 1002)

print(kirirto.action())
print(asuno.action())
print(chypalak.action())



# class Myint:
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return str(self.value)
#
# my_int = Myint(100)
# py_int = 100
# my_list = Myint([1,2,3,4])
# print(my_int)
# print(my_list)
# print(py_int)
