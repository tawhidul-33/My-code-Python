
class Shop:
    def __init__(self,shop_name):
        self.shop_name=shop_name

        self.products=[] #product list


    def view_product_list(self):
        print(f"**View Product List Our {self.shop_name}")
        print('Name\tPrice\tQuantity')
        for item in self.products:
            print(f'{item.name}\t{item.price}\t{item.quantity}')





