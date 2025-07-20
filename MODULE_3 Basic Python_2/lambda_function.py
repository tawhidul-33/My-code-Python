#Basic funtion
def double(num):
    result=num*2
    return result
output=double(44)
print(output)
#or
#lambda funtion
double2 = lambda num:num*2
output=double2(34)
print(output)

#akadhik perameter er khetre
add=lambda x,y:x+y
result=add(10,20)
print(result)

#map() er kaj holo list er vitorer element double ba etc niye kaj kora
num=[10,20,40,32,42,78,20,89,]
double_map=map(lambda x:x*2,num)
print(num)
#print(double_map)
print(list(double_map))# aikhane iteretor output dey ai jonno list use korchi