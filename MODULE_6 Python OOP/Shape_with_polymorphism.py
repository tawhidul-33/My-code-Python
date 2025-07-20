from math import pi
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        return f'somehow area'
class Rectangle(Shape):
    def __init__(self, name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        return pi*self.radius*self.radius
class Sqr(Shape):
    def __init__(self, name):
        super().__init__(name)
    #aikhane area dei nai tar fole sqr a area call korle ..parent er area call hobe

ractangle=Rectangle('Ractangle',12,5)
print(ractangle.area())

circle=Circle('circle',6)
print(circle.area())

sqr=Sqr('sqe')
print(sqr.area())

