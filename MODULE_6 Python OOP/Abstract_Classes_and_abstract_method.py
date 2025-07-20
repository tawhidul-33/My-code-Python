#ABC=Abstract Base Mathod
#abstract mane holo,,kno method abstract ba inforce korle oi method tar child class a baniye use kortei hobe
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Monky(Animal):
    def __init__(self,name):
        self.name=name
        super().__init__()
    def eat(self):
        print('eating banana')
    def move(self):
        print('runing')
lucky=Monky('lucky')
lucky.eat()
lucky.move()