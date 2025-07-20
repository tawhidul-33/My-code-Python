maximum=max(10,20,50,40,99,30)
print('maximum =',maximum)
#or
maximum=max([10,20,50,40,99,30])
print('maximum =',maximum)

minimum=min(10,20,50,40,99,30)
print('minimum =',minimum)

count=len([1,2,3])# koyta element ache ai jonno
print('count =',count)

total=sum([10,20,50,40,99,30])
print('total = ',total)


#Import module
from for_fun_import import double_it
result=double_it(10)
print(result)

#function er short name use
from for_fun_import import double_it as dt
result=dt(10)
print(result)