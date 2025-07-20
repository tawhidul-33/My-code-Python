#Dictionary and Dictionary methods
#Dictionary={'key':'valu','key':'valu','key':'valu'}# key valu piar akare thakbe
person={'name':'siyam','roll':'648433','age':'21'}
print(person)
print(person['name'])#key dele output a valu asbe
print(person['age'])
print(person.keys()) #all keys dekhabe
print(person.values()) #all values dekhabe

# insert new key and valu
person['blood']='B+'
print(person)
print(person['blood'])

#change
person['age']='22'
print(person)

#delete
del person['roll']
print(person)

#dictionary special loop
for key,valu in person.items():
    print(key,valu)
