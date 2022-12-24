class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,deposit):
        self.balance=self.balance+deposit
        print("Deposit Accepted of:",deposit)

    def withdraw(self,withdraw):
        if withdraw<=self.balance:
            self.balance=self.balance-withdraw
            print("Withdrawal Accepted of:",withdraw)
        else:
            print("Funds Unavailable!")

    def print(self):
        print("Account owner:",self.owner)
        print("Account balance:",self.balance)

acct1 = Account('Jose',100)
acct1.print()
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(750)
