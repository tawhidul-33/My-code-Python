class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    #copy product er jonno
    def copy_product(self):
        return Product(self.name, self.price, self.quantity)
    
