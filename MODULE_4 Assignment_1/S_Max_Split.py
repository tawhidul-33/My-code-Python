str=input()
lm=0
cunt=0
sub_str=""
list=[]
for ch in str:
    sub_str=sub_str+ch
    if ch=='L':
        lm+=1
    elif ch=='R':
        lm-=1
    if lm==0:
        cunt+=1
        list.append(sub_str)
        sub_str=""
print(cunt)
for list_part in list:
    print(list_part)

        
    

