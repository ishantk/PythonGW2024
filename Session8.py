"""
    Principle of OOPS:
    1. Think of an Object

    FlightBooking: fromLocation, toLocation, travelDate, numberOfTravllers, travelClass
"""

# 2. Create class of object
# Below class represents the object. It is description of object
class FlightBooking:
    pass

# 3. Create the Real Object from class in Memory
# Below is: Object Construction Statement
booking1 = FlightBooking()
# booking1 is a reference variable, FlightBooking() - represent the object constrution
print(booking1)
print(vars(booking1))

print(id(booking1))
print(hex(id(booking1)))

booking2 = FlightBooking()

# Reference Copy Operation
booking3 = booking1

# Operations on Object
# 1. Write Operation
booking1.fromLocation = "New Delhi"
booking1.toLocation = "Goa"
booking1.travelDate = "15th July, 2024"
booking1.numberOfTravllers = 3
booking1.travelClass = "Economy"

booking2.fromLocation = "Chennai"
booking2.toLocation = "Bangalore"
booking2.travelDate = "25th July, 2024"
booking2.numberOfTravllers = 1
booking2.traveClass = "premium"
booking2.bookedAt = "12:50 17th June, 2024"

# 2. Update Operation
booking3.numberOfTravllers = 2
booking3.fromLocation = "Chandigarh"

# 3. Read Operation
print("booking1 data:")
print(vars(booking1))
print("FROM:", booking1.fromLocation, "TO:", booking1.toLocation)

print("booking2 data:")
print(vars(booking2))
print("FROM:", booking2.fromLocation, "TO:", booking2.toLocation)

# 4. Delete Operation
del booking1.travelClass
print("booking1 data after delete:")
print(vars(booking1))

del booking1

print("booking3 data:")
print(vars(booking3))
print("FROM:", booking3.fromLocation, "TO:", booking3.toLocation)