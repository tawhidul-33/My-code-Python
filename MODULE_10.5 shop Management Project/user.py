from order import Order
class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password


class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def add_product(self,shop,product):
        shop.products.append(product)

    def produc_view(self,shop):
        shop.view_product_list()
        

class Customer(User):
    def __init__(self,shop, name, email, password):
        super().__init__(name, email, password)
        self.shop=shop 
        self.order=Order()

    def find_product(self,product_name):
        for product in self.shop.products:
            if product_name.lower() in product.name.lower():
                return product
        return None
            
    def add_to_cart(self,product_name,quantity):
        product=self.find_product(product_name)
        if product:
            if quantity>product.quantity:
                print("product quantity exceeded!!")
            else:
                copy_prdt=product.copy_product()
                copy_prdt.quantity=quantity
                self.order.carts.append(copy_prdt)
                print('Product added to cart')
    def paybill(self,amount):
        if amount<self.order.total_price():
            print('Payid not successfull')
        else:
            print(f'Payid Successfull {self.order.total_price()} tk')
            for ad_crd_item in self.order.carts:
                org_item=self.find_product(ad_crd_item.name)
                if org_item:
                    org_item.quantity = org_item.quantity - ad_crd_item.quantity
            self.order.clear()


    def view_carts(self):
        print("View Cart list")
        print('Name\tPrice\tQuantity')
        for item in self.order.carts:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print(F'Total Price: {self.order.total_price()}')
    
            
    def view_product(self):
        self.shop.view_product_list()
