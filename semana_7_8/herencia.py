# 1. Crear la clase padre 
class Vehicle: 
    def general_usage(self):
        print("General use: Transportation")

# Clases hijas 
class Car(Vehicle):
    def __init__(self): 
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True 

    def specific_usage(self):
        print("Specific use: Commute to work, vacation with familiy")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motorcyble")
        self.wheels = 2
        self.has_roof = False  

    def specific_usage(self):
        print("Specific use: road trip, racing")

c = Car()
c.general_usage()
c.specific_usage()



