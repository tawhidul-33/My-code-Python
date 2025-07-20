first_num=int(input())
operator=input()
second_num=int(input())
if operator == '+':
    print(first_num+second_num)
elif operator == '-':
    print(first_num-second_num)
elif operator == '*':
    print(first_num*second_num)
elif operator == '/':
    print(first_num/second_num)
else:
    print('Invalid operator')