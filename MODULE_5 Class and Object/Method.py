class phone:
    brand='VIVO'
    price=17000
    clour='sky blue'
    def call(self):
        print("calling one persion")
    def send_sms(self,number,sms):
        text=f'sending sms to : {number} and sms : {sms}'
        return text


my_phone=phone()
print(my_phone.brand)
my_phone.call()
result= my_phone.send_sms('01738438362','I miss you')
print(result)