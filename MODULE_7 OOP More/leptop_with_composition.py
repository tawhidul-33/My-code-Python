# Composition হচ্ছে OOP-এর একটা কনসেপ্ট, যেখানে এক ক্লাসের ভেতরে অন্য ক্লাসের object রাখা হয় — মানে "has-a relationship"।
# যেমন ধরো, একটা Laptop এর মধ্যে CPU, RAM, আর HardDrive থাকে।

# অর্থাৎ, Laptop has a CPU, has a RAM, has a HDD — এটাই Composition.

class CPU:
    def __init__(self,cores):
        self.cores=cores
    def __repr__(self):
        return f'{self.cores}'
class RAM:
    def __init__(self,size):
        self.size=size
    def __repr__(self):
        return f'{self.size}'
class HardDrive:
    def __init__(self,capacity):
        self.capacity=capacity
    def __repr__(self):
        return f'{self.capacity}'

class Leptop:
    def __init__(self,cores,size,capacity):
        self.cpu=CPU(cores) #child class gulu main class a attribute hisabe kaj kore
        self.ram=RAM(size)
        self.hdd=HardDrive(capacity)
    def __repr__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, HDD: {self.hdd}"
lenovo=Leptop(8,12,1000)
print(lenovo)