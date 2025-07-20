from Shop import Shop
from user import User,Seller,Customer
from product import Product
from order import Order


techPata=Shop('TechPata')

#customer interface
def customer():
    name=input('Enter Your Name: ')
    email=input('Enter Your Email: ')
    password=input('Enter Your password: ')
    customer=Customer(techPata,name,email,password)
    while True:

        print(f"\nWelcome Dear {customer.name}!!")
        print('1.View product')
        print('2.Add to Cart')
        print('3.View Cart')
        print('4.Buy')
        print('5.Exit')

        try:
            choice=int(input("Enter Your Choice: "))
        except ValueError:
            print('Invalid Input. Please enter a number between 1-5')
            continue
        if choice==1:
            customer.view_product()
        elif choice==2:
            name = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            customer.add_to_cart(name,qty)
        elif choice==3:
            customer.view_carts()
        elif choice==4:
            try:
               amount = int(input("Enter amount to pay: "))
            except ValueError:
                print('Invalid Input. Please enter ''int''  number')
                continue
            customer.paybill(amount)
        elif choice==5:
            print("Thank you for visiting TechPata. Goodbye!")
            break
        else:
            print('Invalid Input. Please enter a number between 1-5')
#seller interface
def seller():
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    password = input('Enter Your Password: ')
    seller = Seller(name, email, password)

    while True:
        print(f"\nWelcome Seller {seller.name}!")
        print("1. Add Product")
        print("2. View Product List")
        print("3. Exit")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-3")
            continue
        if choice==1:
            p_name=input("Enter product name: ")
            try:
                p_price=int(input("Enter product price: "))
                p_quantity=int(input("Enter product quantity: "))
            except ValueError:
                print("Invalid price or quantity. Please enter valid numbers")
                continue
            product=Product(p_name,p_price,p_quantity)
            seller.add_product(techPata,product)
            print("Product added successfully!")
        elif choice==2:
            seller.produc_view(techPata)
        elif choice==3:
            break
        else:
            print('Invalid Input. Please enter a number between 1-3')

##UI-User Interface
while True:
    print('*<->*WELCOME*<->*')
    print('1.ARE YOU SELER')
    print('2.ARE YOU CUSTOMAR')
    print('3.EXIT')
    try:
       choice=int(input('Enter Your Choice into (1/2/3):'))
    except ValueError:
        print('Invalid Input. Please enter a number between 1-3')
        continue
        
    if choice==1:
        seller()
    elif choice==2:
        customer()
    elif choice==3:
        break
    else:
        print('Invalid Input. Please enter a number between 1-3')
            
    

