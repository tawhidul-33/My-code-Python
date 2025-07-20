#Base class,,parent class,,common attribut+funtion class
#Derived class,,child class,,uncommon attribut+funtion class


#common attribut+funtion class
class Gadget:
    def __init__(self,brand,color,price,origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    def run(self):
        return f'runing lepotp {self.brand}'

#uncommon attribut+funtion class
class Laptop:
    def __init__(self,memory,ssd):
        self.memory=memory
        self.ssd=ssd
    def coding(self):
        return f'learning python code'
    
class Phone(Gadget): #inherit 
    

    def __init__(self,brand,color,price,origin,dual_sim):
        self.dual_sim=dual_sim
        super().__init__(brand,color,price,origin)

    def phone_call(self,number,text):
        return f'sending sms to:{number} with:{text}'
    def __repr__(self):
        return f'phone:{self.brand} price:{self.price} color:{self.color} Yes it is:{self.dual_sim}'


class Camera:
    def __init__(self,pixel):
        self.pixel=pixel
    def change_lens(self):
        pass

my_phone=Phone('iphone','blue',10000,'china','dual sim')
print(my_phone)
print(my_phone.phone_call('01738438362','My number'))
