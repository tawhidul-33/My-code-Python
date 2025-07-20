class phone:
    Brand='VIVO'
    
    def __init__(self,owener,brand,price): #constructor
        self.owener=owener
        self.brand=brand
        self.price=price


    def send_sms(self,number,sms):
        text=f'sending sms to : {number} and sms : {sms}'
        return text
    
my_phone=phone('siyam','oppo',15000)
print(my_phone.owener,my_phone.brand,my_phone.price)

my_dad_phone=phone('Father','samsung',20000)
print(my_dad_phone.owener,my_dad_phone.brand,my_dad_phone.price)

# send_sms method ai khane constructor na,,
# ai jonno je kno object dara call dile aki output asbe
print(my_phone.send_sms('01738438362','miss'))
print(my_phone.Brand)
print(my_dad_phone.send_sms('01738438362','miss'))
print(my_dad_phone.Brand)


