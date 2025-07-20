numbers=[12,14,55,60,75,99,58]

numbers.append(100) #last a add kora
print(numbers)

numbers.insert(0,200)# indx onusare add kora
print(numbers)

numbers.remove(60)# number dile oi number remove hoye jabe
print(numbers)

last=numbers.pop()# last eliment delete kore dibe
print(last)
print(numbers)

if 99 in numbers:     #sorto jodi list a 99 thake 
   indx=numbers.index(99) # ai number er index ber kore dibe 
   print(indx)


numbers.sort()  #sorted korar jonno
print(numbers)

numbers.reverse()
print(numbers)