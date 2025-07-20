#gette: আগে আমরা কোনো private attribute (যেমন __mony) দেখতে চাইলে method (যেমন get_mony()) কল করতাম।
# এখন Getter (@property) দিয়ে method কেই attribute এর মতো দেখতে পারছি,
# মানে সরাসরি object.get_mony লিখলেই হয়ে যাচ্ছে — কোনো () লাগছে না।
# এতে কোড Readable, Clean, আর সুন্দর হচ্ছে।
#even sadharon method a getter use kore attribute er moto access korte parbo

# আগে ➔ private attribute-এর মান পরিবর্তন করতে মেথড (set_name() এর মতো) কল করতে হতো।
# এখন ➔ Setter ব্যবহার করে সেই মেথডকে attribute-এর মতো বানানো যায়,
# মানে সরাসরি object.get_mony = "new value" লিখে আপডেট করা যায়, কোনো মেথড কলের মতো () দরকার হয় না।
#Setter তৈরি করতে হলে আগে অবশ্যই সেই নামের Getter থাকতে হবে।
class User:
    def __init__(self,name,age,mony):
        self._name=name
        self._age=age
        self.__mony=mony
    @property   #getter
    def get_mony(self):
        return self.__mony
    
    #setter
    @get_mony.setter
    def get_mony(self,valu):
        if valu<0:
           print('mony can not be negetive') 
        else:
            self.__mony+=valu


samchu=User('kupa',21,1000)
#print(samchu.__mony) not access because it's private attribute

print(samchu.get_mony)
samchu.get_mony=-1
print(samchu.get_mony)