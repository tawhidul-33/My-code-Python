# Encapsulation = Data hiding + Access control (Public/Protected/Private)
class Bank:
    def __init__(self,halolder_name,intil_deposit):
        self.halolder_name=halolder_name #public atribute
        self._brance='Mirpur10' #protected attribute
        self.__balance=intil_deposit #private attribute
    def deposit(self,amount):
        self.__balance+=amount
    def get_balnce(self):
        return self.__balance
    def Withdrow(self,amount):
        if amount<self.__balance:
             self.__balance = self.__balance - amount
             return amount
        else:
            return f'porjapto balance nai'

rafsun=Bank('Rafsun',40000)
print(rafsun.halolder_name)
rafsun.halolder_name='jichan'# public access korte pare,, thats mean "halolder_name"  public attribut
print(rafsun.halolder_name)
rafsun.deposit(10000) 
#print(rafsun.__balance) # public access korte parena,, thats mean "__balance"  private attribut
print(rafsun.get_balnce())
print(rafsun._brance)
print(rafsun.Withdrow(40000))
print(rafsun.get_balnce())