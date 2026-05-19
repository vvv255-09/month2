from faker import Faker
"""
    Эта библиотека нужна для генерации случайных фейковых данных:
    имён, 
    адресов, 
    email-ов,
    телефонов и т.д.
"""

from colorama import Fore, Style
"""
    Colorama — это библиотека для цветного текста в терминале.
"""

fake = Faker('ru_RU')

print("Faker: фейковые юзеры")

print(Fore.GREEN + "Пользователь" + Style.RESET_ALL)
print(Fore.BLUE + f"  Имя: {fake.name()}" + Style.RESET_ALL)
print(Fore.RED + f"  Email: {fake.email()}" + Style.RESET_ALL)
print(Fore.YELLOW + f"  Телефон: {fake.phone_number()}" + Style.RESET_ALL)
print(Fore.CYAN + f"Город: {fake.city()}" + Style.RESET_ALL)
