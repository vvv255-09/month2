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

#two sum
def two_sum(nums, target):
    """
    Находит два числа в списке nums, сумма которых равна target.
    Возвращает список из двух индексов [i, j].
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return None


nums1 = [2, 7, 11, 15]
target1 = 9
result1 = two_sum(nums1, target1)
i, j = result1
print(f"nums={nums1}, target={target1}")
print(f"Результат: {result1}")
print(f"Проверка: {nums1[i]} + {nums1[j]} = {nums1[i] + nums1[j]}")

