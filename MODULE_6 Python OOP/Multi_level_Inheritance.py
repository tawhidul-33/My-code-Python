class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def move(self):
        pass
    def __repr__(self):
        return f'Vehicle Name: {self.name} Price: {self.price} '
class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self):
        return super().__repr__()+f'Seat: {self.seat} '
class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight=weight
        super().__init__(name, price)
class PickupTruck(Truck):
    def __init__(self, name, price, weight,product):
        self.product=product
        super().__init__(name, price, weight,)
class AcBus(Bus):
    def __init__(self, name, price, seat,temprature):
        self.temprature=temprature
        super().__init__(name, price, seat)
    def __repr__(self):
        print('BUS Details')
        return super().__repr__() + f'Temprature: {self.temprature}'

GreenLine=AcBus('Green Line',10000000,45,'18c')
print(GreenLine)
    