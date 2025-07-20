#Explore Bank withdraw deposit and balance using class
class bank:
    bank='Islamic Bank'
    def __init__(self,balance):
        self.balance=balance
        self.min_withdrow=100
        self.max_withdrow=100000

    def get_balane(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'your new balance {self.balance}')
        
    def withdrow(self,amount):
        if amount<self.min_withdrow:
            print(f'Not withdroe minimum {self.min_withdrow}')
        elif amount>self.max_withdrow:
            print(f'Not withdro Maximum {self.max_withdrow}')
        elif amount<self.balance:
            print(f'Your withdrow Done {amount} tk')
            print(f'Your new balane {self.balance-amount}')
        else:
            print(f'Not withdrow your acount balance {self.get_balane()}')#{self.get_balane()} ba self.balance dile o hobe
    

Grahok=bank(20000)

Grahok.deposit(10000)
Grahok.withdrow(500)

print(Grahok.get_balane())