class Order:
    def __init__(self):
        self.carts=[]
    
    
    def total_price(self):
        sum=0
        for item in self.carts:
            sum=sum+item.price*item.quantity
        return sum
    def clear(self):
        self.carts=[]
         