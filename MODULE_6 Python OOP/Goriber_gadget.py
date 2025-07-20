class Leptop:
    def __init__(self,brand,color,price,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f'runing lepotp {self.brand}'
    def coding(self):
        return f'lerning python code'
    
class Phone:
    def __init__(self,brand,color,price,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim
    def phone_call(self,number,text):
        return f'sending sms to:{number} with:{text}'
    def run(self):
        return f'phone tipteche'

class Camera:
    def __init__(self,brand,color,price,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    def run(self):
        pass
    def change_lens(self):
        pass
