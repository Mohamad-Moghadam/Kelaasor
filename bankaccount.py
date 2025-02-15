class BankAccount:
    def __init__(self, balance: int = 0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print(f"Insufficient funds! ")

    def balance(self):
        return f"{self.__balance}"
