"""
    Driver has a vehicle
    Customer can book Ride(s)

    Identiy Objects with attributes

    Vehicle: reg_number, brand, model, color
    Driver:  name, phone, email, license_number, rating, gender, age, vehicle [1 to 1]

    1 Driver has 1 Vehicle

    Customer: name, phone, email, address, gender, age

    Ride: customer [1 to 1], date, time, from_location, to_location, distance, fare, driver [1 to 1]
    1 Ride has 1 Customer
    1 Ride has 1 Driver
"""

class Vehicle:

    def __init__(self, reg_number="NA", brand="NA", model="NA", color="white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        print(">> ENTER VEHICLE DETAILS")
        self.reg_number = input("Enter Vehcile Registration Number: ")
        self.brand = input("Enter Vehcile Brand: ")
        self.model = input("Enter Vehcile Model: ")
        self.color = input("Enter Vehcile Color: ")

    def show(self):
        print("------------------VEHCILE-----------------")
        print("Number: {} | Brand: {}".format(self.reg_number, self.brand))
        print("Model: {} | Color: {}".format(self.model, self.color))
        print("------------------------------------------")


# vehicle = Vehicle(reg_number="PB10AB1234", brand="Maruti", model="Swift", color="black")
# vehicle = Vehicle()
# vehicle.add_vehicle_details()
# vehicle.show()

# print(vars(vehicle))