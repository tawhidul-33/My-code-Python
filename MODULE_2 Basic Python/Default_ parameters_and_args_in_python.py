def sum(num1,num2,num3=0):
    result=num1+num2+num3
    return result

total=sum(10,20)
print(total)
total=sum(10,20,40)
print(total)

#args
# all_sum(*numbers): aitake bole 'args' jar mane joto iccha parameter pathayte paro 
def all_sum(*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        sum+=num
    print(sum)

all_sum(10,20,30,40)
        
