name = 'siyam\'s molla'
name1="TI Siyam"
name2="""MD Tawhidul Islam
Siyam Molla"""
print(name)
print(name1)
print(name2)
print(name2[3:9])
print(name2[3:9:2])

for chr in name:
    print(chr)

#immutable means you can not change it
# name[0]='g'  # Not possible 
# print(name)

if 'Islam' in name2:
    print("exists")
#Upper to lower and lower to upper  case 
print(name.upper())
print(name.lower())