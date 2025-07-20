from abc import ABC, abstractmethod
from ride import RideRequest,RideMatching
class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount):
        super().__init__(name, email, nid)
        self.current_ride=None
        self.current_location=current_location
        self.wallet =initial_amount

    def display_profile(self):
        print(f'Rider name:{self.name} Email:{self.email} NID:{self.nid}')
    def load_cash(self,amoun):
        if amoun>0:
           self.wallet+=amoun
        else:
            print('Amount less then 0')
    def update_location(self,current_location):
        self.current_location=current_location

    def request_ride(self,ride_sharing,destination,vehicle_type):
        ride_request=RideRequest(self,destination) #aikhane self rider er object hisabe jacche karon aita rider class er moddehi ace tai self dilei hobe
        ride_matching=RideMatching(ride_sharing.drivers)
        ride=ride_matching.find_driver(ride_request,vehicle_type)
        ride.rider=self
        self.current_ride=ride
        print('YAY!! we got a ride')

    def show_curent_ride(self):
        print("Ride Details!!")
        print(f'Ride:{self.name}')
        print(f'Driver:{self.current_ride.driver.name}')
        print(f'Selected Car:{self.current_ride.vehicle.vehicle_type}')
        print(f'Start location:{self.current_ride.start_location}')
        print(f'End location:{self.current_ride.end_location}')
        print(f'Total cost:{self.current_ride.estimated_fare}')


class Driver(User):
    def __init__(self, name, email, nid,current_location):
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet=0
    def display_profile(self):
        print(f'Driver Name: {self.name} Email:{self.email} NID:{self.nid}')
    def accept_ride(self,ride):
        #accept korbo
        ride.start_ride()
        ride.set_driver(self) #aikhane driver er object pathayte hobe .,ar aikhane jehutu Driver class er moddeh tai self mane driver class er object pass hoye geche
    def reach_destination(self,ride):
        ride.end_ride()
    
    