n = int(input()) 
numbers = list(map(int, input().split()))
min_count = float('inf')
flag=0
for num in numbers:
    if num % 2 == 0:
        count = 0
        while num % 2 == 0:
         num = num // 2 
         count += 1
        min_count = min(min_count, count)
    else:
       flag=1
       break
if flag==1:
   print(0)
else:
   print(min_count)
