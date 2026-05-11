
rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        if self.currency not in rates:
            print(f"Валюта {self.currency} не поддерживается")
            return None
        return self.amount * rates[self.currency]

    def __add__(self, other):
        total = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total, "KGS")

    def __sub__(self, other):
        total = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total, "KGS")

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def __truediv__(self, other):
        return Money(self.amount / other, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
result = money1 + money2
print(result)
print(money1 - money2)
print(money1 * 3)
print(money2 / 2)