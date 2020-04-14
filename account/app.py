class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())  # instance variable

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# inheritance from bank account


class Checking(Account):
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking('balance.txt', 1)
checking.transfer(40)
checking.commit()
print(checking.balance)
# account = Account("balance.txt")  # create an object instance
# print(account.balance)
# account.deposit(1300)
# print(account.balance)
# account.commit()
