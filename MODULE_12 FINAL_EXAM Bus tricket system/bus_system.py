from user import Passenger
class BusSystem:

    def __init__(self):
        self.bus_list=[]
        self.passenger_list=[]

 

    def add_bus(self,bus):
        self.bus_list.append(bus)
        print()

    def find_bus(self,bus_number):
        for bus in self.bus_list:
            if bus.bus_number == bus_number:
                return bus
        return None
    
    def book_ticket(self,bus_number,pas_name, phone):
        bus=self.find_bus(bus_number)
        if bus:
            if bus.available_seats()>0:
                bus.book_seat()
                passenger=Passenger(pas_name,phone,bus)
                self.passenger_list.append(passenger)
                print('Book Ticket Successful,fare: 500tk')
            else:
                print('Not Available Seats')
        else:
            print('Not Available Your Choice Bus, Try Others Bus')

    def show_buses(self):
        if len(self.bus_list) == 0:
           print("Not Availabale Bus In This System")
        else:
            for bus in self.bus_list:
                print(bus)

