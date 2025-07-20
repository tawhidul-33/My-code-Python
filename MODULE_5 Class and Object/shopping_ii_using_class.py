class shopping:
    def __init__(self,name):
        self.name=name
        self.card=[]
    def add_to_card(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}#dictionary kore rakha
        self.card.append(product) #dictionare list a pathano 
    def checkout(self,amount):
        total_cost=0
        for itm in self.card:
            total_cost += itm['price']*itm['quantity']
        if amount<total_cost:
            print(f'{total_cost-amount} tk lagbe')
        else:
            print(f'{amount-total_cost} tk obosistho thake' )

siyam=shopping('siyam')
siyam.add_to_card('alu',50,6)
siyam.add_to_card('dim',12,2)
siyam.add_to_card('rice',60,5)

print(siyam.card)
siyam.checkout(10000)


