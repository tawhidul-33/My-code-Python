num = input()
numbrs = input().split()

delete_num = 0
fre_num = {}


for item in numbrs:
    if item in fre_num:
        fre_num[item] += 1
    else:
        fre_num[item] = 1

for key, valu in fre_num.items():
    
    if valu > int(key):
        delete_num += valu - int(key)
    elif valu < int(key):
        delete_num += valu
print(delete_num)