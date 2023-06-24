class BankAccount:
    def __init__(self):
        self.account_num=input("enter account no:")
        self.balance=input("enter balance:")
        self.date_opening=input("enter date_opening:")
        self.customer_name=input("enter customer_name:")
    def deposit(self,amount):
        self.balance+=amount
        print(amount,"is deposited!!!")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient")
        else:
            self.balance+=amount
            print(amount,"is withdrawn!!!")
    def check_balance(self):
        print("ur balance is", self.balance)
