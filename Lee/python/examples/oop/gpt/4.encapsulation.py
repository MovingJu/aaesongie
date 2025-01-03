class BankAccount(object):
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            raise ValueError("Input amount cannot less than Zero.")

    def withdraw(self, amount):
        if amount >= 0:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                raise ValueError("Not enough balance is in your account.")
        else:
            raise ValueError("Input amount cannot less than Zero.")

    def get_balance(self):
        return self.__balance
    
    
if __name__ == "__main__":
    p1 = BankAccount(50000)
    p1.deposit(500)
    # p1.deposit(-500)
    p1.withdraw(5050)
    print(p1.get_balance())