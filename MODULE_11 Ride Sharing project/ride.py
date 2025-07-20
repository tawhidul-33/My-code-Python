from datetime import datetime #built in vabe time import korlam
from vehicle import Car,Bike
class rideSharing:
    def __init__(self,company_name):
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[] #koto gulu ride hoyeche tai
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __repr__(self):
        return f'company name:{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'
class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=self.calculate_fare(vehicle.vehicle_type) #orthat, amader total koto taka lagbe jayte 
        self.vehicle=vehicle
    def set_driver(self,driver):#aikhne driver class er object anbo
        self.driver=driver
    def start_ride(self):
        self.start_time=datetime.now()
    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet=self.rider.wallet-self.estimated_fare
        self.driver.wallet=self.driver.wallet+self.estimated_fare
    #totat cost-fare
    def calculate_fare(self,vehicle):
        distance=10
        fare_per_km={
            'car':30,
            'bike':20,
            'cng':25
        }
        return distance*fare_per_km.get(vehicle)
    def __str__(self):
        return f'Ride details started {self.start_location} to {self.end_location}'

        
class RideRequest:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location
class RideMatching:
    def __init__(self,drivers):
        self.available_driver=drivers

    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_driver)>0:
            print('loking for drivers...')
            driver=self.available_driver[0]
          
            if vehicle_type=='car':
                vehicle=Car('car','23DF2',30)
            elif vehicle_type=='bike':
                vehicle=Bike('bike','125GH',50)
            ride=Ride(ride_request.rider.current_location,ride_request.end_location,vehicle)
            driver.accept_ride(ride)
            return ride
