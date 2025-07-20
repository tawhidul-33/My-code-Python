#Home_work
class calculator:
    brand="casio MS1900"
    #add
    def add(self,num1,num2):
        result=num1+num2
        return result
    #sub
    def sub(self,num1,num2):
        result=num1-num2
        return result
    #mul
    def mul(self,num1,num2):
        result=num1*num2
        return result
    #div
    def div(self,num1,num2):
        result=num1//num2
        return result
calculation=calculator()
    
print(calculation.add(20,10))
print(calculation.sub(20,10))
print(calculation.mul(20,10))
print(calculation.div(20,10))