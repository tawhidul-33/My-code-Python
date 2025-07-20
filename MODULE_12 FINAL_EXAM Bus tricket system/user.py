class Bus:
    def __init__(self,bus_name,bus_number,route,total_seats):
        self.bus_name=bus_name
        self.bus_number=bus_number
        self.route=route
        self.total_seats=total_seats
        self.booked_seats=0
    def __repr__(self):
        return f'Bus_name: {self.bus_name} Bus_NO: {self.bus_number} Route: {self.route} Total_seats: {self.total_seats} Available seats: {self.available_seats()}'
    
    def available_seats(self):
       avl_st=self.total_seats-self.booked_seats
       return avl_st
    
    def book_seat(self):
        if self.available_seats()>0:
           self.booked_seats+=1
         
class Passenger:
    def __init__(self,pas_name,phone,bus):
        self.pas_name=pas_name
        self.phone=phone
        self.bus=bus
        self.fare='500 tk'

class Admin:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,username,password):
        if self.username == username and self.password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password")
            return False

        
        






