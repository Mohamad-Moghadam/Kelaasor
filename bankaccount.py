class BankAccount:
    def __init__(self, balance: int = 0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print(f"Insufficient funds! ")

    def balance(self):
        return f"your balance: {self.__balance}"


account = BankAccount()

amount_of_deposit = int(input("how much cash do you want to deposit? "))
amount_of_withdrawal = int(input("how much cash do you want to withdraw? "))

account.deposit(amount_of_deposit)
account.withdraw(amount_of_withdrawal)

print(account.balance())
