class bank:
    def __init__(self,name,accno,type,balance):
        self.name =name
        self.accno=accno
        self.type=type
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def display(self):
        print("your account balance is :" , self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficient balance")
        else:
            self.balance-=amount
        self.display() 
    
def main():
    p1=None
    while 1:
        choice=int(input("1.create\n2.deposit\n3.withdraw\n4.display\n5.exit"))
        if choice==1:
            acc_name=input("Enter your accnt name: ")
            acc_num=int(input("Enter your accnt number: "))
            acc_type=input("Enter accnt type: ")
            acc_bal=0
            p1=bank(acc_name,acc_num,acc_type,acc_bal)
        elif choice==2:
            amount=int(input("enter the amount to deposit: "))
            p1.deposit(amount)
        elif choice==3:
            amount=int(input("enter the amount to withdraw: "))
            p1.withdraw(amount)
        elif choice==4:
            p1.display()
        else:
            exit()



if __name__=="__main__":
    main()
