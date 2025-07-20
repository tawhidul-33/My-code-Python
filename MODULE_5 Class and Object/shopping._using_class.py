class shopping:
    def __init__(self,name):
        self.name=name
        self.card=[]
    def add_to_card(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.card.append(product)

siyam=shopping('siyam')
siyam.add_to_card('alu',50,6)
siyam.add_to_card('dim',12,2)
siyam.add_to_card('rice',60,5)

ruhul=shopping('ruhul')
ruhul.add_to_card('morich',60,2)
ruhul.add_to_card('piyaj',18,5)
ruhul.add_to_card('oil',50,15)

print(ruhul.card)
print(siyam.card)