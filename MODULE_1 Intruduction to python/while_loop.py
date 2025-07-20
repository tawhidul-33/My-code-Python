num=1
while num<=10:
    print(num)
    num=num+1

print("Break") 

num1=1
while num1<=10:
    print(num1)
    num1=num1+1
    if num1==5:
        break

print("continue")

num2=0
while num2<=10:
    num2=num2+1
    if num2%2!=0:
        continue
    print(num2)
    