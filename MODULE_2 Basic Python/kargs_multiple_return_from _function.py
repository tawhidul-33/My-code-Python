def full_name(first,last):
    name=f'{first} {last}' #or, name=first+' '+last
    print(name)

full_name('siyam','molla')
#or,
full_name(last='molla',first='siyam') # seriyal mantain na korle o nhoy

#args er advence  kargs
def full_name(first,last,**kargs):#args er advence  kargs'**'
    # name=f'{first} {last} {args}'#for normal args
    # print(name) 
    print('args er advence  kargs = ',kargs['title'])

full_name('siyam','molla',title='tawhidul',title2='islam')


#multy perameter return
def multy_prm_retn(num1,num2):
    sum=num1+num2
    mul=num1*num2
    sub=num1-num2
    return sum,sub,mul
result=multy_prm_retn(10,5)
print('multy perameter return = ',result)