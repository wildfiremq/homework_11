class Money:
    def __init__(self, currency, amount): # конструктор,який ініціалізує атрибути currency та amount з вхідними параметрами
        self.currency = currency
        self.amount = amount

    def __str__(self):                  #повертає рядок, який містить суму грошей та її валюту
        return f"{self.amount} {self.currency}"

    def __add__(self, other):             #додаємо
        if self.currency == other.currency:
            return Money(self.currency, self.amount + other.amount)
        else:
            raise ValueError("No common currency found")            # різні валюти

    def __sub__(self, other):           #віднімиємо
        if self.currency == other.currency:
            return Money(self.currency, self.amount - other.amount)
        else:
            raise ValueError("No common currency found")              # різні валюти

if __name__ == "__main__":

        usd_money = Money('USD', 50)
        eur_money = Money('EUR', 40)

        # Виведення сум грошей
        print(usd_money)  # output: 50 USD
        print(eur_money)  # output: 40 EUR

        # Додавання сум грошей у різних валютах
        try:
            sum_money = usd_money + eur_money  # raises ValueError: No common currency found
        except ValueError as e:
            print(str(e))

        # Додавання сум грошей у спільній валюті
        usd_money_2 = Money('USD', 30)

        sum_money = usd_money + usd_money_2
        print(sum_money)  # output: 80 USD