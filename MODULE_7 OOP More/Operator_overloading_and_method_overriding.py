# Overriding:
# Parent ক্লাসের মেথডকে Child ক্লাসে একই নাম রেখে নতুন করে লিখে দেয়া।
# এখানে মেথডের নাম, প্যারামিটার — একই থাকে, শুধু Body বদলে যায়।

# Method Overloading:
# একই নামের মেথড বারবার তৈরি করা হয়, কিন্তু প্যারামিটারের সংখ্যা বা টাইপ আলাদা থাকে।
# কাজের ধরন প্যারামিটারের উপর নির্ভর করে।

#একই নামের মেথডে বারবার প্যারামিটার পরিবর্তন করা — এটাকেই Method Overloading বলে।

# ak kothay method er name peramater sob akoi thake thokhon take overriding bole
# and jokhon method same thake but paremater change hoy bare kobe tahole overloding hoy

#Operator Overloading: মানে হলো ➔ সাধারন +, -, * এর মতো অপারেটরগুলোর default behavior কে customized করা।
# ➔ এখানে মেথডের নাম এবং প্যারামিটার ফিক্সড থাকে।
# ➔ তুমি শুধু ব্যাবহার পরিবর্তন করো।
class Person:
    def  __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print('vat,mach,mangso,polaw')
    def exercise(self):#aikhane raise er maddhome overriding korar jonno inforce kora hocche
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        super().__init__(name, age, height, weight)
        self.team=team
    #Parent class er "def eat(self):" method ta ke Overriding korteche
    def eat(self):
        print("vegetables")
    def exercise(self):
        print('Exercise kore gham jhoray')
    # + sign operator overloding   
    def __add__(self,others):
        return self.age + others.age
    # * sign operator overloding   
    def __mul__(self,others):
        return self.weight*others.weight
    # > sign operator overloding   
    def __gt__(self,others):
        return self.age>others.age

Sakib=Cricketer('Sakib',38,68,75,'BD')
musi=Cricketer('Musi',35,60,70,'BD')
Sakib.eat()
Sakib.exercise()

#method overloding
#plus(+)sign overloding kortechi
print(10+20)
print('sakib'+'rakib')
print([1,2,3]+[4,5])
print(Sakib+musi)
print(Sakib*musi)
print(Sakib>musi)