from ride import Ride,RideMatching,RideRequest,rideSharing
from user import Rider,Driver
from vehicle import Car,Bike
niye_jaw=rideSharing('Niye_jaw')
rahim=Rider('Rahim','rm@.com',753852,'Mohakhali',1200)
niye_jaw.add_rider(rahim)
kolimuddin=Driver('Kolimuddin','km@gmail.com',951357,'Gulsan')
niye_jaw.add_driver(kolimuddin)
rahim.request_ride(niye_jaw,'uttora','car')
kolimuddin.reach_destination(rahim.current_ride)
rahim.show_curent_ride()
print(niye_jaw)