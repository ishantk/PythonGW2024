from Session10C import Vehicle
from Session10D import Driver
from Session11 import Customer
from Session11E import Ride

# Driver Application
driver = Driver()
driver.add_driver_details()

# Customer Application
customer = Customer()
customer.add_customer_details()

# Server
ride = Ride()
ride.add_ride_details()
# ride.customer = Customer()
# ride.customer.add_customer_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("RIDE BOOKED....")
ride.show()