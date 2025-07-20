# Abstract class:
# ➔ "তোমাকে এই method বানাতেই হবে! না বানালে error দিবো!" (Forcefully)

# Polymorphism:
# ➔ "আমার একটা method আছে, তুমি চাইলে override করে নিজের style এ চালাও। না চাইলে parent এরটা use করো।" (No Force)

#polymorphism concept: aki methot er vinno vinno rup..mane bohurupi, aiti polymorphism 
class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print('Animal making some sound')
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print('meow meow')
class dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('ghew ghew')
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
    
don=Cat('real sound')
don.make_sound()

jon=dog('local hero')
jon.make_sound()

milky=Cow('Home animal')
milky.make_sound() #jokhon tar nijer class a 'make_sound' na diya hoy tokhin parent class a je defolt make sound diya ace oitay chole jabe

#object gula ke list a rekhe ,,loop kore er sound output
list=[don,jon,milky]
for obj in list:
    obj.make_sound()