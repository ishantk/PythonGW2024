"""
    Principle of OOPS:
    1. Think of an Object

    FlightBooking: fromLocation, toLocation, travelDate, numberOfTravllers, travelClass
"""

# 2. Create class of object
# Below class represents the object. It is description of object
class FlightBooking:
    
    # Default Constructor in Python
    # self is reference variable, which will hold the hashcode of current object
    def __init__(self):
        print("self:", self)
        self.fromLocation = "New Delhi"
        self.toLocation = "Bengaluru"
        self.travelDate = "18th June, 2024"
        self.numberOfTravllers = 1
        self.travelClass = "Economy"


    # Parameterized Constructor
    def __init__(self, fromLocation, toLocation, travelDate, numberOfTravllers, travelClass):
        print("self:", self)
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.travelDate = travelDate
        self.numberOfTravllers = numberOfTravllers
        self.travelClass = travelClass

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Booking Data:")
        print("FROM:", self.fromLocation, "TO:", self.toLocation)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

booking1 = FlightBooking("NewDelhi", "Chandigarh", "18th June, 2024", 2, "economy")
print("booking1:", booking1)
print("booking1 data:")
# print(vars(booking1))
booking1.show()

booking2 = FlightBooking("Chennai", "Bengaluru", "18th June, 2024", 1, "premium")
print("booking2:", booking1)
print("bookin2 data:")
#print(vars(booking2))
booking2.show()

# Throw Error
# booking3 = FlightBooking()


"""
HW: Code below 3 Objects
    Restaurant
    Menu
    Dish
"""