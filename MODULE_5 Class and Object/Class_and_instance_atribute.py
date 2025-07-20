# class shop:
#     shopingmall='jamuna'

#     card=[] # class attribute ,,thats mean method er bahire attribute
#     def __init__(self,buyer):
#         self.buyer=buyer
#         print(buyer)
    
#     def add_to_card(self,item):
#         self.card.append(item)
    
# mehezabin=shop('Mehezabin')
# mehezabin.add_to_card('dress')
# mehezabin.add_to_card('shoes')
# mehezabin.add_to_card('phone')
# print(mehezabin.card)

# nishu=shop('Nisho')
# nishu.add_to_card('sunglass')
# nishu.add_to_card('watch')
# nishu.add_to_card('pant')
# print(nishu.card)


#Instance attribute
class shop:
    shopingmall='jamuna'


    def __init__(self,buyer):
        self.buyer=buyer
        self.card=[]#instance attribute,thats means method er vitore attribut
        print(buyer)
    
    def add_to_card(self,item):
        self.card.append(item)
    
mehezabin=shop('Mehezabin')
mehezabin.add_to_card('dress')
mehezabin.add_to_card('shoes')
mehezabin.add_to_card('phone')
print(mehezabin.card)

nishu=shop('Nisho')
nishu.add_to_card('sunglass')
nishu.add_to_card('watch')
nishu.add_to_card('pant')
print(nishu.card)
