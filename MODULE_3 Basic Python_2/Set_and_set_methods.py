#list->[]
#tuple->()
#Set->{}

#set: unique items collection ,, not duplicate
num_set={10,20,30,50,10,40,60,30,80}
print(type(num_set))
print(num_set)
#add
num_set.add(100)
print(num_set)
#remove
num_set.remove(60)
print(num_set)

for item in num_set:
    print(item)

if 10 in num_set:
    print('exists')

A={1,3,5,7}
B={1,2,3,4,5,}
print(A&B) #common
print(A|B) #common and uncommon 