class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            # instance variable(define within a method of a class)
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# inheritance from bank account


class Checking(Account):  # create a subclass out of a base class
    '''This class generates checking account objects(Doc strings)'''
    # class varible can be shared with all the instance of that class
    accout_type = "checking"

    def __init__(self, filepath, fee):  # constructor
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):  # method
        self.balance = self.balance - amount - self.fee


checking = Checking('balance.txt', 1)  # instantiation
checking.transfer(40)
checking.commit()
print(checking.balance)
print(checking.accout_type)
print(checking.__doc__)  # provide information  about the class
# account = Account("balance.txt")  # create an object instance
# print(account.balance)
# account.deposit(1300)
# print(account.balance)
# account.commit()
