numbers=[12,14,55,60,75,99,58]
odd=[]
for num in numbers:
    if num%2!=0:
        odd.append(num)
print(odd)

#or
odd_num=[num for num in numbers if num%2!=0]
print(odd_num)


