class BankAccount:      #банківський рахунок
    def __init__(self, balance, interest_rate=0):
        self._balance = balance             #число, що представляє баланс рахунку.
        self.interest_rate = interest_rate  #число, що представляє відсоткову ставку на рахунку.

    def deposit(self, amount):         #конструктор, що додає задану суму на рахунок
        self._balance += amount

    def withdraw(self, amount):         #що знімає задану суму з рахунку
        if amount > self._balance:
            raise ValueError("Not enough balance")  #якщо недостатньо коштів на рахунку,
        self._balance -= amount

    def add_interest(self):                 #додає на рахунок проценти відповідно до відсоткової ставки.
        interest = self._balance * self.interest_rate
        self._balance += interest

    @property
    def balance(self):
        return self._balance

    @classmethod
    def create_checking_account(cls, balance):
        return cls(balance, interest_rate=0.25)


if __name__ == "__main__":
    account = BankAccount(1000)

    print(account.balance)  # output: 1000

    account.deposit(500)            # Додавання коштів
    print(account.balance)  # output: 1500

    try:                            # Зняття коштів
        account.withdraw(2000)  # raises ValueError: Not enough balance
    except ValueError as e:
        print(str(e))


    account.add_interest()              # Додавання відсотків
    print(account.balance)  # output: 1500

    # Використання методу класу
    acc2 = BankAccount.create_checking_account(500)
    acc2.deposit(500)
    acc2.add_interest()
    print(acc2.balance)  # 1002.5