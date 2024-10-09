class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print(f'{self.owner}様、入金金額：{amount},残高は：{self.balance}')
        else :
            print('入金金額を0円以上にください。')

    def withdraw(self , amount):
        if amount > self.balance:
            print(f'{self.owner}様、残高不足です。')
        elif amount <= 0:
            print('引き出し金額は0円以上にください。')
        else :
            self.balance -= amount
            print(f'{self.owner}様、引き出し金額は{amount}円です。残高は：{self.balance}円です。')

    def check_balance(self):
        print(f'{self.owner}様、残高は：{self.balance}円です。')

account = BankAccount('Alice', 1000)
account.deposit(300)
account.withdraw(800)
account.check_balance()