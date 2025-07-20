from user import Bus,Admin
from bus_system import BusSystem
system=BusSystem()

#Admin interface
def fun_admin():
    while True:
        print('1. Add Bus')
        print('2. View All Buses')
        print('3. Logout')
        try:
            choice=int(input("Enter Your Choice (1/2/3)"))
        except ValueError:
            print("Invalid input. Please enter a valid number into (1/2/3)")
            continue
        if choice==1:
            try:
                
                name = input("Enter bus name to add: ")
                number = input("Enter bus number to add: ")
                route = input("Enter bus route to add: ")
                seats = int(input("Enter total seats to add: "))
                bus=Bus(name,number, route, seats)
                system.add_bus(bus)
                print('Bus Added Successful')
            except ValueError:
                print("Not Added,Seats must be a number")
                continue
        elif choice==2:
            print('Our Service Buses')
            system.show_buses()
        elif choice==3:
            break
        else:
            print("Invalid input. Please enter a valid number into (1/2/3)")


            
#main interface
while True:
    print('1. Admin Login')
    print('2. Book Ticket')
    print('3. View Buses')
    print('4. Exit')
    try:
        choice=int(input('Enter Your Choice (1/2/3/4)'))
    except ValueError:
        print("Invalid input. Please enter a valid number into (1/2/3/4)")
        continue
    if choice==1:
        admin=Admin('admin','1234')
        username = input("Enter Admin username: ")
        password = input("Enter Admin password: ")
        if admin.login(username,password):
            print("Admin login Successfully")
            fun_admin()
        else:
            print("Login failed! Invalid username or password")

    elif choice==2:
        bus_number = input("Enter your choices bus number: ")
        pas_name = input("Enter your name: ")
        pas_phone = input("Enter your phone number: ")
        system.book_ticket(bus_number,pas_name,pas_phone)
    elif choice==3:
         system.show_buses()
    elif choice==4:
        break
    else:
        print("Invalid input. Please enter a valid number into (1/2/3/4)")
 


        

