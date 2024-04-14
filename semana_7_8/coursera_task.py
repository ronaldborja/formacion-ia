class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "white"
        self.seating_capacity = None 

    def set_seating_capacity(self, seatin_capacity):
        self.seating_capacity = seatin_capacity

    def display_properties(self):
        print("Properties of the vehicule")
        print("Maximum Speed: ",self.max_speed)
        print("Mileage", self.mileage)
        print("Color: ",self.color)
        print("Seating capacity", self.seating_capacity)

    
o1 = Vehicle(200, 50000)
o1.set_seating_capacity(5)
o1.display_properties()

print(" ")

o2 = Vehicle(180, 76000)
o2.set_seating_capacity(4)
o2.display_properties()
    


