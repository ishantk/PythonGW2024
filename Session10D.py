"""
    Driver:  
    name, phone, email, license_number, rating, gender, age, vehicle [1 to 1]

"""

from Session10C import Vehicle

class Driver:

    def __init__(self, name="NA", phone="NA", email="NA", 
                 license_number="NA", rating=2.5, 
                 gender="NA", age=18, vehicle=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.license_number = license_number
        self.rating = rating
        self.gender = gender
        self.age = age
        self.vehicle = vehicle

    def add_driver_details(self):
        print(">> ENTER DRIVER DETAILS")
        self.name = input("Enter Driver Name: ")
        self.phone = input("Enter Driver Phone: ")
        self.email = input("Enter Driver Email: ")
        self.license_number = input("Enter Driver License Number: ")
        self.rating = float(input("Enter Driver Rating: "))
        self.gender = input("Enter Driver Gender: ")
        self.age = int(input("Enter Driver Age: "))
       
        # 1 to 1 Mapping
        # 1 Driver has 1 Vechile
        self.vehicle = Vehicle() # Object Construction
        self.vehicle.add_vehicle_details()

    def show(self):
        print("------------------DRIVER-----------------")
        print("Name: {} | Phone: {}".format(self.name, self.phone))
        print("Email: {} | License: {}".format(self.email, self.license_number))
        print("Rating: {} | Gender: {} | Age: {}".format(self.rating, self.gender, self.age))
        print("------------------------------------------")

        self.vehicle.show()

