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

class Ride:

    def __init__(self, customer=None, date="20th June, 2024", time="12:00", 
                 from_location="Home", to_location="Work", otp=3027,
                 distance=4, fare=200, driver=None):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.otp = otp
        self.distance = distance
        self.fare = fare
        self.driver = driver


    def add_ride_details(self):
        print(">> ENTER RIDE DETAILS")
        self.from_location = input("Enter From Location: ")
        self.to_location = input("Enter To Location: ")
        
    def link_customer(self, customer):
        self.customer = customer
    
    def link_driver(self, driver):
        self.driver = driver

    def show(self):

        self.customer.show()

        print("------------------RIDE-----------------")    
        print("FROM: {} | TO: {}".format(self.from_location, self.to_location))
        print("DISTANCE: {} | FARE: {}".format(self.distance, self.fare))
        print("DATE: {} | TIME: {}".format(self.date, self.time))
        print("OTP: {} ".format(self.otp))
        print("------------------------------------------")

        self.driver.show()
