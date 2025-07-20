# #local beriavle sudu function er moddeh kaj kore ,,global fun access payna

# balance=300# global veriable
# def buy_things(item,price):
#     balance=500 # aita local veriable hisabe kaj korbe
#     print('previous balanse valu',item,balance)
#     #balance=balance-price
#     print('after buying balanse valu',balance)
# print(balance)# global veriable
# buy_things('sunglass',100)



#global fun access pawer jonno funtion a local veriable er global lekte hobe

balance=300 #global veriable
def buy_things(item,price):
    global balance #aita akhon golbal veriable hisabe kaj korbe
    print('previous balanse valu',item,balance)
    balance=balance-price
    print('after buying balanse valu',balance)
buy_things('sunglass',100)
print(balance)